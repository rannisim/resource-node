from pytest import fixture

from app.repositories.resource_repository import ResourceRepository

RESOURCE = {'key': 'value'}

class TestResourceRepository(object):
    @fixture
    def repository(self):
        yield ResourceRepository()

    def test_read(self, repository):
        assert repository.read() is None

    def test_save(self, repository):
        repository.save(RESOURCE)

        assert repository.read() == RESOURCE

