import requests

from flask import current_app
from flask import abort
import requests

def get_or_log_error(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.HTTPError as e:
        current_app.logger.error("HTTP Error %s", e)
        abort(response.status_code)
    except requests.exceptions.ConnectionError as e:
        current_app.logger.error("Error %s", e)
        abort(500)
