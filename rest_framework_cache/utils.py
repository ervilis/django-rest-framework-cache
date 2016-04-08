from .cache import cache
from .registry import cache_registry
from .settings import api_settings


def get_cache_key(instance, serializer, protocol):
    """Get cache key of instance"""
    params = {"id": instance.pk,
              "app_label": instance._meta.app_label,
              "model_name": instance._meta.object_name,
              "serializer_name": serializer.__name__,
              "protocol": protocol}

    return api_settings.SERIALIZER_CACHE_KEY_FORMAT.format(**params)


def get_all_cache_keys(instance):
    """Get all possibles cache keys for given instance"""
    keys = []
    serializers = cache_registry.get(instance.__class__)
    for serializer in serializers:
        keys.append(get_cache_key(instance, serializer, 'http'))
        keys.append(get_cache_key(instance, serializer, 'https'))
    return keys


def clear_for_instance(instance):
    """Clear the cache for the given instance"""
    keys = get_all_cache_keys(instance)
    cache.delete_many(keys)
