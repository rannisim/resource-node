from pytest import fixture

from app.clients.resource_node_client import ResourceNodeClient


HOST ='http://localhost:8080'
RESOURCE = {'test': 'integration'}

class TestResourceNodeClient(object):
    @fixture
    def client(self):
        yield ResourceNodeClient(HOST)

    def test_save_and_read(self, client):
        client.save(RESOURCE)

        actual_result = client.read()

        assert actual_result == RESOURCE

