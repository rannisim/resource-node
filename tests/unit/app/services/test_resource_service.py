from unittest.mock import MagicMock

from pytest import fixture

from app.services.resource_service import ResourceService

RESOURCE = {'key1': 'val', 'key2': 'val'}

class TestResourceService(object):
    @fixture
    def service(self):
        self.__in_memory_repository = MagicMock()
        self.__external_repository = MagicMock()

        yield ResourceService(self.__in_memory_repository, self.__external_repository)

    def test_read_from_user_when_result_is_cached(self, service):
        self.__in_memory_repository.read.return_value = RESOURCE

        actual_resource = service.read(False)

        assert actual_resource == RESOURCE

    def test_read_from_user_when_result_is_not_cached(self, service):
        self.__in_memory_repository.read.return_value = None
        self.__external_repository.read.return_value = RESOURCE

        actual_resource = service.read(False)

        assert actual_resource == RESOURCE

    def test_read_from_peer_when_result_is_cached_not_cached(self, service):
        self.__in_memory_repository.read.return_value = None
        self.__external_repository.read.return_value = RESOURCE

        actual_resource = service.read(True)

        assert actual_resource == None

    def test_save_from_user(self, service):
        service.save(RESOURCE, False)

        self.__in_memory_repository.save.assert_called_with(RESOURCE)
        self.__external_repository.save.assert_called_with(RESOURCE)

    def test_save_from_peer(self, service):
        service.save(RESOURCE, True)

        self.__in_memory_repository.save.assert_called_with(RESOURCE)
        self.__external_repository.save.assert_not_called()
