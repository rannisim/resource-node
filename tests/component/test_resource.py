import requests

NODE_1_HOST ='http://localhost:8080'
NODE_2_HOST ='http://localhost:9080'
RESOURCE_PATH = '/api/resource'

RESOURCE_1 = {'test': 'componet1'}
RESOURCE_2 = {'test': 'componet2'}

class TestResource(object):
    def test_save_and_read_from_the_same_node(self):
        node_1_url = '{}{}'.format(NODE_1_HOST, RESOURCE_PATH)

        requests.post(node_1_url, json=RESOURCE_1)

        actual_response_body = requests.get(node_1_url).json()

        assert actual_response_body == RESOURCE_1

    def test_save_and_read_from_different_nodes(self):
        node_1_url = '{}{}'.format(NODE_1_HOST, RESOURCE_PATH)
        node_2_url = '{}{}'.format(NODE_2_HOST, RESOURCE_PATH)

        requests.post(node_1_url, json=RESOURCE_2)

        actual_response_body = requests.get(node_2_url).json()

        assert actual_response_body == RESOURCE_2