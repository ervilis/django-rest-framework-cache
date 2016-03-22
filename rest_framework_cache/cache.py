from django.core.cache import cache, caches

from .settings import api_settings
from .exceptions import ImproperlyConfigured


try:
    cache_backend = api_settings.DEFAULT_CACHE_BACKEND
    if cache_backend != "default":
        cache = caches[cache_backend]
except KeyError:
    raise ImproperlyConfigured("'{}' is a invalid CACHE_BACKEND".format(
        api_settings.DEFAUL_CACHE_BACKEND))
