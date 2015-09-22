import unittest
import pyjs

class TestCase(unittest.TestCase):
    def test_create_context(self):
        cx = pyjs.Context()
        self.assertTrue(cx)

    def test_eval(self):
        cx = pyjs.Context()
        cx.eval("function exp() {return 10;}");
        resp = cx.eval('exp();')
        self.assertEqual(resp, 10)
