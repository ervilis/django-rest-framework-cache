import unittest

from rest_framework_cache.utils import get_cache_key, get_all_cache_keys
from rest_framework_cache.registry import cache_registry

from .models import TestModel
from .serializers import TestSerializer


class GetCacheKeyTestCase(unittest.TestCase):

    def test_ok(self):
        instance = TestModel()
        instance.id = 1000
        serializer = TestSerializer()
        key = get_cache_key(instance, serializer.__class__, 'http')
        self.assertEqual(key, "http.tests.TestModel.TestSerializer:1000")


class GetAllCacheKeyTestCase(unittest.TestCase):

    def setUp(self):
        cache_registry.register(TestSerializer)

    def test_ok(self):
        instance = TestModel()
        instance.id = 1000
        keys = get_all_cache_keys(instance)
        self.assertEqual(keys, ["http.tests.TestModel.TestSerializer:1000",
                                "https.tests.TestModel.TestSerializer:1000"])
