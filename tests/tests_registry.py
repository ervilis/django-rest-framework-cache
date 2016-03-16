import unittest

from rest_framework_cache.registry import CacheRegistry
from rest_framework_cache.exceptions import AlreadyRegistered


class TestModel:
    pass


class TestSerializer:

    class Meta:
        model = TestModel


class CacheRegistryTestCase(unittest.TestCase):

    def test_empty_registry(self):
        registry = CacheRegistry()
        self.assertEqual(registry._registry, {})

    def test_register_ok(self):
        registry = CacheRegistry()
        registry.register(TestSerializer)
        expected_registry = {
            TestModel: [TestSerializer],
        }
        self.assertEqual(registry._registry, expected_registry)

    def test_alread_registered(self):
        registry = CacheRegistry()
        registry.register(TestSerializer)
        with self.assertRaises(AlreadyRegistered):
            registry.register(TestSerializer)
