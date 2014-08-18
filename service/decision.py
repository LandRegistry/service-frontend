import requests
import json
from service import app


class Decision(object):

    def __init__(self, decision_url):
        self.api = '%s/decisions' % decision_url

        #signed_token
        #transaction_id

    def post(self, data):
        json_data = self._payload(data)
        headers = {'content-type': 'application/json'}
        app.logger.info("Sending data %s to the decision at %s" % (json_data, self.api))
        try:
            decision_response = requests.post(self.api, data=json_data, headers=headers).json()
            url = decision_response['url']
            app.logger.info('Sending data to the chosen url at %s' % url)
            downstream_response = requests.post(url, data)
            return (decision_response, downstream_response)
        except requests.exceptions.RequestException as e:
            app.logger.error("Could not effect decision at %s: Error %s" % (self.api, e))
            raise RuntimeError

    def __repr__(self):
        return self.api

    def _payload(self, data):
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
