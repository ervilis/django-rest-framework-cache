from .cache import cache
from .utils import get_all_cache_keys


def clear_instance(sender, instance, **kwargs):
    """Calls cache cleaner for current instance"""
    keys = get_all_cache_keys(instance)
    cache.delete_many(keys)
