from rest_framework import serializers

from .cache import cache
from .exceptions import AlreadyRegistered
from .registry import registry
from .settings import api_settings
from .utils import get_cache_key


class CachedSerializerMixin(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
        Checks if the representation of instance is cached and adds to cache
        if is not.
        """
        key = get_cache_key(instance, self.__class__)
        cached = cache.get(key)
        if cached:
            return cached

        result = super(CachedSerializerMixin, self).to_representation(instance)
        cache.set(key, result, api_settings.DEFAULT_CACHE_TIMEOUT)
        return result

    def __new__(cls, *args, **kwargs):
        """We must register all cached serializers into registry"""
        klass = super(CachedSerializerMixin, cls).__new__(cls, *args, **kwargs)
        try:
            registry.register(cls)
        except AlreadyRegistered:
            pass
        return klass
