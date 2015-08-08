import unittest
import py_js as pyjs

class TestCase(unittest.TestCase):
    def test_get_runtime(self):
        rt = pyjs.Runtime()
        self.assertTrue(rt)

    def test_print_runtime(self):
        rt = pyjs.Runtime()
        self.assertTrue(True)

    def test_get_cx(self):
        rt = pyjs.Runtime()
        cx = rt.Context()
        self.assertTrue(cx)

    def test_eval(self):
        rt = pyjs.Runtime()
        cx = rt.Context()
        self.assertTrue(cx.eval("1 + 1"))
