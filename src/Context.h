#ifndef _PYJS_CONTEXT_H_
#define _PYJS_CONTEXT_H_

#include <jsapi.h>
#include <Python.h>

#include "Runtime.h"
#include "utils/macros.h"

typedef struct {
    PyObject_HEAD
    JSContext *cx;
} PyJS_Context;

extern PyTypeObject PyJS_ContextType;
#endif
