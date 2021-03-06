#include <jsapi.h>
#include <Python.h>

#include "Context.h"
#include "Runtime.h"

static bool jsInited = false;

PyJS_Runtime *
PyJS_Runtime_new()
{
    PyJS_Runtime *self = (PyJS_Runtime *)PyJS_RuntimeType.tp_alloc(&PyJS_RuntimeType, 0);

    LOG("[PyJS_Runtime_new] jsInited %d\n", jsInited);
    if (!jsInited) {
        JS_Init();
        jsInited = true;
    }

    JSRuntime *rt = JS_NewRuntime(1024 * 8 * 1024, JS_NO_HELPER_THREADS);
    LOG("[PyJS_Runtime_new] Succesfully created\n");
    if (!rt) {
        PyErr_SetString(PyExc_RuntimeError, "Cannot create javascript runtime");
        PyJS_RuntimeType.tp_free((PyObject *)self);
        return nullptr;
    }
    self->rt = rt;

    return self;
}

void
PyJS_Runtime_free(PyJS_Runtime *self)
{
    JS_DestroyRuntime(self->rt);
    PyJS_RuntimeType.tp_free((PyObject *)self);
}

// Python.h definitions

static PyMethodDef methods[] = {
    {"Context", (PyCFunction)(*[](PyJS_Runtime *rt) -> PyObject * {
        return PyObject_CallObject((PyObject *)&PyJS_ContextType, Py_BuildValue("(O)", rt)); 
    }), METH_NOARGS, "Create context"},
    {nullptr}
};

PyTypeObject PyJS_RuntimeType {
    PyObject_HEAD_INIT(nullptr)
    0,
    "py_js.Runtime",
    sizeof(PyJS_Runtime), 0,
    
    (destructor)(PyJS_Runtime_free),
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
    0,
    (newfunc)([](PyTypeObject *type, PyObject *args, PyObject *kwds) -> PyObject* {
        return (PyObject *)PyJS_Runtime_new();
    })
};
