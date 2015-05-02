#include <Python.h>
#include <jsapi.h>
#include "Runtime.h"

PyObject *
PyJS_Runtime_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PyJS_Runtime* self;
    // TODO: allocated space should point trough configuration
    JSRuntime *rt = JS_NewRuntime(16L * 1024 * 1024, JS_USE_HELPER_THREADS);
    if (!rt) {
        PyErr_SetString(PyExc_RuntimeError, "Cannot create javascript runtime");
        return nullptr;
    };

    self->rt = rt;

    return (PyObject *)self;
}

PyTypeObject PyJS_RuntimeType {
    PyObject_HEAD_INIT(nullptr)
    0,
    "pyjs.Runtime",
    sizeof(PyJS_Runtime), 0,
    
    0, //destructor
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

    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0, // init
    0, // alloc
    PyJS_Runtime_new, // new
};
