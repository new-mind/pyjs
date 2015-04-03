import unittest
import pyjs

class TestCase(unittest.TestCase):
    def test_get_runtime(self):
        pyjs.Runtime()
