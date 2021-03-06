#include <Python.h>
#include <jsapi.h>

#include "Context.h"
#include "Runtime.h"

static PyMethodDef methods[] = {
    {nullptr},
};

PyMODINIT_FUNC
initpy_js(void)
{
    PyObject *mod = Py_InitModule("py_js", methods);

    if (PyType_Ready(&PyJS_RuntimeType) < 0)
        return;

    if (PyType_Ready(&PyJS_ContextType) < 0)
        return;

    PyModule_AddObject(mod, "Runtime", (PyObject *)&PyJS_RuntimeType);
};
