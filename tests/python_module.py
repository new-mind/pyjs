import unittest
import json
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

    def test_set_global(self):
        cx = pyjs.Context()
        cx.setGlobal('global', 12)
        self.assertEqual(cx.eval('global'), 12)

    def test_set_global_obj(self):
        cx = pyjs.Context()
        cx.setGlobal('global', {'a': 1})
        resp = cx.eval('global;')
        self.assertEqual(resp, '[Object]')
