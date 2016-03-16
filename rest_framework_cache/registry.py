from .exceptions import AlreadyRegistered


class CacheRegistry:

    def __init__(self):
        self._registry = {}

    def register(self, serializer):
        model = serializer.Meta.model

        if model not in self._registry:
            self._registry[model] = []

        if serializer in self._registry[model]:
            raise AlreadyRegistered("Serializer {} is already registered"
                                    .format(model.__name__))

        self._registry[model].append(serializer)


# This global object represents the default CacheRegistry, for the common case.
# You can instantiate CacheRegistry in your own code to create a custom
# register.
registry = CacheRegistry()
