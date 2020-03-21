from os import environ

from app import app_init

print(app_init)

from app.clients.resource_node_client import ResourceNodeClient
from app.controllers.health_controller import HealthController
from app.controllers.resource_controller import ResourceController
from app.repositories.resource_repository import ResourceRepository
from app.routes import create_routes
from app.services.resource_service import ResourceService

PEER_RESOURCE_NODE_HOST = environ.get('PEER_RESOURCE_NODE_HOST', default='localhost')


health_controller = HealthController()

in_memory_resource_repository = ResourceRepository()
external_resource_repository = ResourceNodeClient(PEER_RESOURCE_NODE_HOST)
resource_service = ResourceService(in_memory_resource_repository, external_resource_repository)
resource_controller = ResourceController(resource_service)

create_routes(app_init.app, health_controller, resource_controller)

if __name__ == '__main__':
      app_init.app.run(port=8080, host='0.0.0.0')