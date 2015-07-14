#include <jsapi.h>
#include <Python.h>

PyObject *convert(JSContext *cx, JS::RootedValue *val)
{
    PyObject *a;
    if (val->isNull()) {
        return Py_BuildValue("");
    }

    if (val->isUndefined()) {
        return Py_BuildValue("");
    }

    if (val->isBoolean()) {
        return a;
    }

    if (val->isInt32()) {
        return Py_BuildValue("i", val->toInt32());
    }

    if (val->isDouble()) {
        return Py_BuildValue("d", val->toDouble());
    }

    if (val->isString()) {
        return Py_BuildValue("s", JS_EncodeString(cx, val->toString()));
    }
    
    if (val->isObject()) {
        return a;
    }
}
