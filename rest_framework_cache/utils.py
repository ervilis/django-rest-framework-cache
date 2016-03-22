from .registry import registry
from .settings import api_settings


def get_cache_key(instance, serializer):
    """Get cache key of instance"""
    params = {"id": instance.pk,
              "app_label": instance._meta.app_label,
              "model_name": instance._meta.object_name,
              "serializer_name": serializer.__name__}

    return api_settings.SERIALIZER_CACHE_KEY_FORMAT.format(**params)


def get_all_cache_keys(instance):
    """Get all possibles cache keys for given instance"""
    keys = []
    serializers = registry.get(instance.__class__)
    for serializer in serializers:
        keys.append(get_cache_key(instance, serializer))
    return keys
