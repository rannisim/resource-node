import json

import requests

RESOURCE_PATH = '/api/resource'
RESOURCE_PARAMS = {'peer_request': True}


class ResourceNodeClient(object):
    def __init__(self, resource_node_host):
        self.__resource_url = '{host}/{path}'.format(host=resource_node_host, path=RESOURCE_PATH)

    def read(self):
        try:
            response = requests.get(self.__resource_url, params=RESOURCE_PARAMS)
            return response.json()
        except:
            return {}

    def save(self, resource):
        try:
            requests.post(self.__resource_url, json=resource, params=RESOURCE_PARAMS)
        except:
            return
