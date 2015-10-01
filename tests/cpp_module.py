import unittest
import py_js

class ConvertTestCase(unittest.TestCase):
    def test_convert_undefined(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('undefined')
        self.assertEqual(res, None)

    def test_convert_null(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('null')
        self.assertEqual(res, None)

    def test_convert_int32(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('1')
        self.assertEqual(res, 1)

    def test_convert_double(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('1.1')
        self.assertEqual(res, 1.1)

    def test_convert_bool(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('false')
        self.assertEqual(res, False)

    def test_convert_bool(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('false')
        self.assertEqual(res, False)

    def test_convert_string(self):
        rt = py_js.Runtime()
        cx = rt.Context()
        res = cx.eval('"2"')
        self.assertEqual(res, "2")
