import unittest
from app.common.utils.patterDesign import singleton

class PatterDesignTest(unittest.TestCase):
    def test_singleton(self):
        @singleton
        class TestClass:
            pass
        instance_one = TestClass()
        instance_second = TestClass()
        self.assertEqual(instance_second,instance_one)