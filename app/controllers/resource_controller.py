import json

from flask import request, current_app

APP_JSON = 'application/json'

class ResourceController(object):

    def __init__(self, resource_service):
        self.__resource_service = resource_service

    def read(self):
        """
        :param: peer_request - used to distinguish between user calls and internal calls.
                            This was added in order to prevent endless recursive call between the nodes.
        :return: The saved Json object if there is one or return an empty object if none was found
        """
        is_peer_request = request.args.get("peer_request", default=False)

        resource = self.__resource_service.read(is_peer_request)

        response_body = resource if resource else {}

        return current_app.response_class(status=200, response=json.dumps(response_body), content_type=APP_JSON)

    def save(self):
        """
                :param: peer_request - used to distinguish between user calls and internal calls.
                                    This was added in order to prevent endless recursive call between the nodes.
                :return: Status 200 when save was successful
        """
        is_peer_request = request.args.get("peer_request", default=False)

        request_body = request.get_json()

        self.__resource_service.save(request_body, is_peer_request)

        return current_app.response_class(status=200)
