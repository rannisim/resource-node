import json
from unittest import TestCase
from unittest.mock import MagicMock

from flask import Flask
from pytest import fixture

from app.controllers.resource_controller import ResourceController

IS_PEER_REQUEST = False
EMPTY_RESPONSE = {}
RESOURCE = {'key': 'value'}
RESOURCE_JSON = json.dumps(RESOURCE)

app = Flask(__name__)


class TestResourceController(object):

    @fixture()
    def controller(self):
        self.__service = MagicMock()

        with app.test_request_context(data=RESOURCE_JSON, content_type='application/json'):
            yield ResourceController(self.__service)

    def test_read(self, controller):
        self.__service.read.return_value = RESOURCE

        response = controller.read()

        actual_result = (response.status_code, response.json)
        expected_result = (200, RESOURCE)

        assert  actual_result == expected_result

        self.__service.read.assert_called_with(IS_PEER_REQUEST)

    def test_read_resource_not_exists(self, controller):
        self.__service.read.return_value = None

        response = controller.read()

        actual_result = (response.status_code, response.json)
        expected_result = (200, EMPTY_RESPONSE)

        assert actual_result == expected_result

        self.__service.read.assert_called_with(IS_PEER_REQUEST)

    def test_save(self, controller):
        response = controller.save()

        assert response.status_code == 200

        self.__service.save.assert_called_with(RESOURCE, IS_PEER_REQUEST)


