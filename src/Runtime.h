#ifndef _PYJS_RUNTIME_H_
#define _PYJS_RUNTIME_H_

#include <Python.h>
#include <jsapi.h>
#include "structmember.h"

class PyJS_Runtime
{
    PyObject_HEAD
    JSRuntime *rt;

    public:
        PyJS_Runtime();
        ~PyJS_Runtime();
};

extern PyTypeObject PyJS_RuntimeType;
#endif
