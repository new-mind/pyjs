import unittest
import py_js as pyjs

class TestCase(unittest.TestCase):
    def test_expose_function(self):
        r = pyjs.Runtime()
        c = r.Context()

        c.eval('function exp() { return 10; }')
        resp = c.eval('exp();')
        self.assertEqual(resp, 10)
