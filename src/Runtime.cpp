#include <Python.h>
#include <jsapi.h>
#include "Runtime.h"

PyObject *
PyJS_Runtime_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
{
    PyJS_Runtime* self = reinterpret_cast<PyJS_Runtime *>(type->tp_alloc(type, 0));

    // TODO: allocated space should point trough configuration
    JSRuntime *rt = JS_NewRuntime(16L * 1024 * 1024, JS_USE_HELPER_THREADS);
    if (!rt) {
        PyErr_SetString(PyExc_RuntimeError, "Cannot create javascript runtime");
        return nullptr;
    };

    self->rt = rt;

    return (PyObject *)self;
}

int PyJS_Runtime_init(PyJS_Runtime *self, PyObject *args, PyObject *kwds)
{
}

void PyJS_Runtime_free(PyJS_Runtime *self)
{
}

PyTypeObject PyJS_RuntimeType {
    PyObject_HEAD_INIT(nullptr)
    0,
    "pyjs.Runtime",
    sizeof(PyJS_Runtime), 0,
    
    (destructor)PyJS_Runtime_free, //destructor
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
    (initproc)PyJS_Runtime_init, // init
    0, // alloc
    (newfunc)PyJS_Runtime_new, // new
};
