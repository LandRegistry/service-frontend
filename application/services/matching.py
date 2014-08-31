import logging
import requests

from flask import session
from requests.exceptions import (
    HTTPError,
    ConnectionError
)

from application import app

MATCHING_URL = app.config['MATCHING_URL']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

def check_user_match(user):
    logger.info("Checking user %s against matching service %s" %(user, MATCHING_URL))

    if 'lrid' in session:
        logger.info('Already have LRID for user %s' % user)
        return True

    headers = {'Content-type': 'application/json'}
    data  = user.to_json_for_match()

    try:
        resp = requests.post(
                url='%s/match' % MATCHING_URL,
                data=data,
                headers=headers)

        response.raise_for_status()
        data = resp.json()
        logger.info('Reponse lrid %s' % data['lrid'])

        #NOTE session cookie might not be best place
        #for this longer term
        session['lrid'] = data['lrid']
        return True

    except (HTTPError, ConnectionError) as e:
        logger.error("Error trying to check for user match: %s", e)
        return False
    except:
        logger.error("Unknown error trying to check for user match")
        return False

