#include <Python.h>
#include <jsapi.h>
#include "Runtime.h"

PyJS_Runtime::PyJS_Runtime()
{
    JSRuntime *rt = JS_NewRuntime(16L * 1024 * 1024, JS_USE_HELPER_THREADS);
    if (!rt) {
        PyErr_SetString(PyExc_RuntimeError, "Cannot create javascript runtime");
    }

    this->rt = rt;
}

PyJS_Runtime::~PyJS_Runtime()
{
    Py_XDECREF(this->rt);
    this->ob_type->tp_free((PyObject *)this);
    JS_DestroyRuntime(this->rt);
}

static PyMethodDef methods[] = {
    {}
};

PyTypeObject PyJS_RuntimeType {
    PyObject_HEAD_INIT(nullptr)
    0,
    "pyjs.Runtime",
    sizeof(PyJS_Runtime), 0,
    
    (destructor)(*[](PyJS_Runtime *self) -> void {
        delete self;
    }),
    0,
    0,
    0,
    0,
    0,

    0,
    0,
    0,

    0,
    0,
    0,
    0,
    0,

    0,

    Py_TPFLAGS_DEFAULT, // tp_flags

    "Create runtime object", // Documentation string

    0,

    0,

    0,

    0,

    0,
    0,

    methods,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    (initproc)(*[](PyJS_Runtime *self, PyObject *args, PyObject *kwds) -> int {
        return 0;
    }),
    0, // alloc
    (newfunc)(*[](PyTypeObject *type, PyObject *args, PyObject *kwds) -> PyObject* {
        return (PyObject *)new PyJS_Runtime();
    })
};
