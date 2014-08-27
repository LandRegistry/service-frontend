import json
import logging

from flask import current_app

import requests
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

headers = {'content-type': 'application/json'}

def post_to_decision(url, data):
    decision_response = _post_decision(url, data).json()
    url = decision_response['url']
    downstream_response = _post_downstream(url, data)
    return (decision_response, downstream_response)

def _post_decision(url, data):
    try:
        json_data = _payload_decision(data)
        logger.info("Sending data %s to the decision at %s" % (json_data, url))
        return requests.post(
                url,
                data=json_data,
                headers=headers,
                auth=HTTPBasicAuth(
                    current_app.config['BASIC_AUTH_USERNAME'],
                    current_app.config['BASIC_AUTH_PASSWORD']))
    except requests.exceptions.RequestException as e:
        logger.error("Could not effect decision at %s: Error %s" % (url, e))
        raise RuntimeError

def _post_downstream(url, data):
    try:
        json_data = _payload_downstream(data)
        logger.info("Sending data %s to the downstream at %s" % (json_data, url))
        return requests.post(
                url,
                data=json_data,
                headers=headers,
                auth=HTTPBasicAuth(
                    current_app.config['BASIC_AUTH_USERNAME'],
                    current_app.config['BASIC_AUTH_PASSWORD']))
    except requests.exceptions.RequestException as e:
        logger.error("Could not effect decision at %s: Error %s" % (url, e))
        raise RuntimeError

def _payload_decision(data):
    return json.dumps({
           "action": "change-name-marriage",
           "data": {
               "iso-country-code": data['marriage_country']
           },
           "context": {
               "session-id": "123456",
               "transaction-id": "ABCDEFG"
           }
       })

def _payload_downstream(data):
    # date hack until we can settle on data formats/handling/ser/deser
    dt = data.pop('marriage_date')
    data['marriage_date'] = long(dt.strftime("%s"))

    data['application_type'] = 'change-name-marriage'
    return json.dumps(data)
