import json

from flask import current_app

APP_JSON = 'application/json'

class HealthController(object):

    def health_check(self):
        response = {'healthy': True}

        return current_app.response_class(response=json.dumps(response), status=200, content_type=APP_JSON)