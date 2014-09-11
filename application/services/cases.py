import json
import logging
import requests

from requests.auth import HTTPBasicAuth
from flask import current_app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

headers = {'content-type': 'application/json'}


def post_to_cases(action, data):
    return _post_case(action, data)


def _post_case(action, data):
    try:
        json_data = _payload_case(action, data)
        url = current_app.config['CASES_URL'] + "/cases"
        logger.info("Sending data %s to the cases at %s with action type %s" % (json_data, url, action))
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


def _payload_case(action, data):
    return json.dumps({
        "application_type": action,
        "title_number": data['title_number'],
        "submitted_by": data['proprietor_full_name'],
        "request_details": {
            "action": action,
            "data": _fmt(data),
            "context": {
                "session-id": "123456",
                "transaction-id": "ABCDEFG"
            }
        }
    })

def _fmt(data):
    # date hack until we can settle on data formats/handling/ser/deser
    dt = data.pop('marriage_date')
    data['marriage_date'] = long(dt.strftime("%s"))

    data['application_type'] = 'change-name-marriage'
    return json.dumps(data)
