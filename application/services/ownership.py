import logging
import requests
import uuid
import json

from flask import session

from application import app

OWNERSHIP_URL = app.config['OWNERSHIP_URL']

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

def check_user_is_owner(user, title_number):

    logger.info("Checking title number %s ownership service at %s" %(title_number,OWNERSHIP_URL))

    if 'lrid' not in session:
        logger.info("LRID not known for user %s so can't check ownership" % user)
        return False

    headers = {'Content-type': 'application/json'}
    data = json.dumps({"title_number":title_number})

    resp = requests.post(
            url='%s/owners' % OWNERSHIP_URL,
            data=data,
            headers=headers)

    logger.info('Response status %s' % resp.status_code)

    if resp.status_code == 200:
        data = resp.json()
        owners = data['owners']
        logger.info('Response owners %s' % owners)
        for match in owners:
            if session['lrid'] == match['lrid']:
                return True
        else:
            return False
    else:
        logger.info('Unable to establish ownership of %s by %s' % (title_number, user))
        return False
