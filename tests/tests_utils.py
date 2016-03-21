import unittest

from rest_framework_cache.utils import get_cache_key
from .models import TestModel
from .serializers import TestSerializer


class GetCacheKeyTestCase(unittest.TestCase):

    def test_ok(self):
        instance = TestModel()
        instance.id = 1000
        serializer = TestSerializer()
        key = get_cache_key(instance, serializer)
        self.assertEqual(key, "tests.TestModel.TestSerializer:1000")
