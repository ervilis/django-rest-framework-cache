from .settings import api_settings


def get_cache_key(instance, serializer):
    """Get cache key of instance"""
    params = {"id": instance.pk,
              "app_label": instance._meta.app_label,
              "model_name": instance._meta.object_name,
              "serializer_name": serializer.__class__.__name__}

    return api_settings.SERIALIZER_CACHE_KEY_FORMAT.format(**params)
