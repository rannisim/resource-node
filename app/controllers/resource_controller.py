import json

from flask import request, current_app

APP_JSON = 'application/json'

class ResourceController(object):

    def __init__(self, resource_service):
        self.__resource_service = resource_service

    def read(self):
        is_peer_request = request.args.get("peer_request", default=False)

        resource = self.__resource_service.read(is_peer_request)

        response_body = resource if resource else {}

        return current_app.response_class(status=200, response=json.dumps(response_body), content_type=APP_JSON)

    def save(self):
        is_peer_request = request.args.get("peer_request", default=False)

        request_body = request.get_json()

        self.__resource_service.save(request_body, is_peer_request)

        return current_app.response_class(status=200)
