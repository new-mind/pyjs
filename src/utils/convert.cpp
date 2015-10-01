#include <jsapi.h>
#include <Python.h>

PyObject *convert(JSContext *cx, JS::RootedValue *val)
{
    if (val->isNull()) {
        return Py_BuildValue("");
    }

    if (val->isUndefined()) {
        return Py_BuildValue("");
    }

    if (val->isBoolean()) {
        return val->toBoolean() ? Py_True : Py_False;
    }

    if (val->isInt32()) {
        return Py_BuildValue("i", val->toInt32());
    }

    if (val->isDouble()) {
        return Py_BuildValue("d", val->toDouble());
    }

    if (val->isString()) {
        JS_BeginRequest(cx);
        char * str = JS_EncodeString(cx, val->toString());
        JS_EndRequest(cx);

        return Py_BuildValue("s", str);
    }
    
    // TODO: object converting not implemented
    if (val->isObject()) {
        return Py_BuildValue("s", "[Object]");
    }
}
