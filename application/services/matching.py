import logging
import sys

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
    logger.debug("Checking user %s against matching service %s" % (user, MATCHING_URL))

    if 'lrid' in session:
        logger.debug('Already have LRID for user %s' % user)
        return True

    headers = {'Content-type': 'application/json'}
    data = user.to_json_for_match()

    try:
        response = requests.post(
            url='%s/match' % MATCHING_URL,
            data=data,
            headers=headers)

        response.raise_for_status()
        data = response.json()
        logger.debug('Reponse lrid %s' % data['lrid'])

        # NOTE we are using flask-kvsession with sqlalchemy as
        #storage so session data is not sent client
        session['lrid'] = data['lrid']
        session['roles'] = data['roles']
        return True

    except (HTTPError, ConnectionError) as e:
        logger.error("Error trying to check for user match: %s", e)
        return False
    except:
        e = sys.exc_info()[0]
        logger.error("Unknown error trying to check for user match: %s" % e)
        return False

def get_client_lrid(user):
    data = user.to_json_for_match()
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post(
            url='%s/match' % MATCHING_URL,
            data=data,
            headers=headers)

        response.raise_for_status()
        data = response.json()
        return data.get('lrid', None)

    except (HTTPError, ConnectionError) as e:
        logger.error("Error trying to check for lrid for: %s" % data)
        return False
    except:
        e = sys.exc_info()[0]
        logger.error("Unknown error trying to get lrid for: %s" % data)
        logger.error("Error: %s" % e)
        return False
