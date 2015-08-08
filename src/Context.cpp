#include <Python.h>
#include <jsapi.h>

#include "Context.h"
#include "Runtime.h"
#include "utils/convert.h"

using namespace JS;

static JSClass global_class = {
    "global",
    JSCLASS_GLOBAL_FLAGS,
    JS_PropertyStub, JS_DeletePropertyStub, JS_PropertyStub, JS_StrictPropertyStub,
    JS_EnumerateStub, JS_ResolveStub, JS_ConvertStub, nullptr,
    nullptr, nullptr, nullptr, JS_GlobalObjectTraceHook
};

PyObject *
PyJS_Context_eval(PyJS_Context *cx, const char *code)
{
    RootedObject global(cx->cx, JS_NewGlobalObject(cx->cx, &global_class, nullptr, DontFireOnNewGlobalHook));
    RootedValue rval(cx->cx);

    {
        JSAutoCompartment ac(cx->cx, global);
        OwningCompileOptions opts(cx->cx);
        JS_InitStandardClasses(cx->cx, global);
        Evaluate(cx->cx, global, opts, code, strlen(code), &rval);
    }

    return convert(cx->cx, &rval);
}

// Python.h definitions

static PyMethodDef methods[] = {
    {"eval", (PyCFunction)(*[](PyJS_Context *cx, PyObject *args) -> PyObject * {
        char *str;
        PyArg_ParseTuple(args, "s", &str);
        return PyJS_Context_eval(cx, str);
    }), METH_VARARGS, "Evaluate javascript"},
    {nullptr}
};

PyTypeObject PyJS_ContextType {
    PyObject_HEAD_INIT(nullptr)
    0,
    "py_js.Runtime.Context",
    sizeof(PyJS_Context), 0,
    
    (destructor)(*[](PyJS_Context *self) -> void {
        JS_DestroyContext(self->cx);
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

    "Create context", // Documentation string

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
    (initproc)(*[](PyJS_Context *self, PyObject *args, PyObject *kwds) -> int {
        return 0;
    }),
    0, // alloc
    (newfunc)(*[](PyTypeObject *type, PyObject *args, PyObject *kwds) -> PyObject* {
        PyJS_Runtime *rt;
        PyArg_ParseTuple(args, "O", &rt);
        PyJS_Context *self = (PyJS_Context *)type->tp_alloc(type, 0);
        self->cx = JS_NewContext(rt->rt, 8 * 1024);
        return (PyObject *)self;
    })
};
