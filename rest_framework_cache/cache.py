from django.core.cache import caches

from .settings import api_settings
from .exceptions import ImproperlyConfigured


try:
    cache = caches[api_settings.DEFAULT_CACHE_BACKEND]
except KeyError:
    raise ImproperlyConfigured("'{}' is a invalid CACHE_BACKEND".format(
        api_settings.DEFAUL_CACHE_BACKEND))
