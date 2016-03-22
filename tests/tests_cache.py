import imp

from django.core.cache.backends.locmem import LocMemCache
from django.core.cache.backends.filebased import FileBasedCache
from django.test import TestCase


class CacheBackendTestCase(TestCase):

    def test_default_backend(self):
        from rest_framework_cache.cache import cache

        self.assertEqual(cache.get('404'), None)

    def test_locmem_backend(self):
        settings = {
            'CACHES': {
                'default': {
                    'BACKEND': 'django.core.cache.backends.filebased.'
                               'FileBasedCache',
                    'LOCATION': '/tmp/rfcache_tests',
                },
                'other': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                    'LOCATION': 'other-snowflake',
                }
            },
            'REST_FRAMEWORK_CACHE': {
                'DEFAULT_CACHE_BACKEND': 'other'
            }
        }
        with self.settings(**settings):
            from rest_framework_cache import cache

            cache = imp.reload(cache)

        self.assertTrue(isinstance(cache.cache, LocMemCache))
        self.assertEqual(cache.cache.get('404'), None)

    def test_filebased_backend(self):
        settings = {
            'CACHES': {
                'default': {
                    'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
                    'LOCATION': 'other-snowflake',
                },
                'other': {
                    'BACKEND': 'django.core.cache.backends.filebased.'
                               'FileBasedCache',
                    'LOCATION': '/tmp/rfcache_tests',
                },
            },
            'REST_FRAMEWORK_CACHE': {
                'DEFAULT_CACHE_BACKEND': 'other'
            }
        }
        with self.settings(**settings):
            from rest_framework_cache import cache

            cache = imp.reload(cache)

        self.assertTrue(isinstance(cache.cache, FileBasedCache))
        self.assertEqual(cache.cache.get('404'), None)
