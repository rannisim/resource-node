class ResourceService(object):

    def __init__(self,
                 in_memory_resource_repository,
                 external_resource_repository):
        self.__in_memory_resource_repository = in_memory_resource_repository
        self.__external_resource_repository = external_resource_repository

    def read(self, is_peer_request):
        entity = self.__in_memory_resource_repository.read()

        if is_peer_request:
            return entity

        return entity if entity is not None else self.__external_resource_repository.read()

    def save(self, resource, is_peer_request):
        self.__in_memory_resource_repository.save(resource)

        if not is_peer_request:
            self.__external_resource_repository.save(resource)