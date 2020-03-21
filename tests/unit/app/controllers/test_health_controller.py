from flask import Flask
from pytest import fixture

from app.controllers.health_controller import HealthController

app = Flask(__name__)


class TestHealthController(object):
    @fixture
    def controller(self):
        with app.app_context():
            yield HealthController()

    def test_health_check(self, controller):
        response = controller.health_check()

        actual_result = (response.status_code, response.json)
        expected_result = (200, {'healthy': True})


        assert actual_result == expected_result
