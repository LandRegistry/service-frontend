import json
import logging
import requests

from requests.auth import HTTPBasicAuth
from flask import current_app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

headers = {'content-type': 'application/json'}


def post_to_cases(data):
    return _post_case(data)


def _post_case(data):
    try:
        json_data = _payload_case(data)
        url = current_app.config['CASES_URL'] + "/cases"
        logger.info("Sending data %s to the cases at %s" % (json_data, url))
        return requests.post(
            url,
            data=json_data,
            headers=headers,
            auth=HTTPBasicAuth(
                current_app.config['BASIC_AUTH_USERNAME'],
                current_app.config['BASIC_AUTH_PASSWORD']))
    except requests.exceptions.RequestException as e:
        logger.error("Could not save case at %s: Error %s" % (url, e))
        raise RuntimeError


def _payload_case(data):
    return json.dumps({
        "application_type": "change-name-marriage",
        "title_number": data['title_number'],
        "submitted_by": data['proprietor_previous_full_name'],
        "request_details": {
            "action": "change-name-marriage",
            "data": {
                "iso-country-code": data['marriage_country']
            },
            "context": {
                "session-id": "123456",
                "transaction-id": "ABCDEFG"
            }
        }
    })