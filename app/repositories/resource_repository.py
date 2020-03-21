class ResourceRepository(object):
    def __init__(self):
        self.__resource = None

    def read(self):
        return self.__resource

    def save(self, resource):
        self.__resource = resource