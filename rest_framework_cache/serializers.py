from rest_framework import serializers

from .settings import api_settings
from .utils import get_cache_key
from .cache import cache


class CachedSerializerMixin(serializers.ModelSerializer):

    def to_representation(self, instance):
        """
        Checks if the representation of instance is cached and adds to cache
        if is not.
        """
        key = get_cache_key(instance, self)
        cached = cache.get(key)
        if cached:
            return cached

        result = super(CachedSerializerMixin, self).to_representation(instance)
        cache.set(key, result, api_settings.DEFAULT_CACHE_TIMEOUT)
        return result
