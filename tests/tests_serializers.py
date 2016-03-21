import mock
import unittest

from rest_framework_cache.serializers import CachedSerializerMixin
from .serializers import TestSerializer
from .models import TestModel


class TestCachedSerializer(CachedSerializerMixin, TestSerializer):
    pass


class GetCacheKeyTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_module = "rest_framework_cache.serializers.cache"
        instance = TestModel()
        instance.id = 1000
        self.serializer = TestCachedSerializer(instance)
        self.expected_data = {"id": 1000, "name": ""}

    def test_cache_miss(self):
        with mock.patch(self.mock_module) as mock_cache:
            mock_cache.get.return_value = None
            data = self.serializer.data

        self.assertEqual(data, self.expected_data)
        self.assertTrue(mock_cache.get.called)
        self.assertTrue(mock_cache.set.called)

    def test_cache_hit(self):
        with mock.patch(self.mock_module) as mock_cache:
            mock_cache.get.return_value = self.expected_data
            data = self.serializer.data

        self.assertEqual(data, self.expected_data)
        self.assertTrue(mock_cache.get.called)
        self.assertFalse(mock_cache.set.called)
