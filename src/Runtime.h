#ifndef _PYJS_RUNTIME_H_
#define _PYJS_RUNTIME_H_

#include <Python.h>
#include <jsapi.h>
#include "structmember.h"
#include "utils/macros.h"

typedef struct {
    PyObject_HEAD
    JSRuntime *rt;
} PyJS_Runtime;

extern PyTypeObject PyJS_RuntimeType;
#endif
