#include <Python.h>

PyObject *
pyjs_runtime(PyObject *self, PyObject *args)
{
    PyObject *a;
    return a;
}

static PyMethodDef methods[] {
    {"Runtime", pyjs_runtime, 0, NULL},
};

PyMODINIT_FUNC
initpyjs(void)
{
    (void) Py_InitModule("pyjs", methods);
}
