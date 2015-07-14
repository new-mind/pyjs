#ifndef _PYJS_UTILS_CONVERT_
#define _PYJS_UTILS_CONVERT_

#include <jsapi.h>
#include <Python.h>

PyObject *convert(JSContext *cx, JS::RootedValue *val);

#endif
