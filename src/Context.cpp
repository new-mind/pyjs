#include <Python.h>
#include <jsapi.h>

#include "Context.h"
#include "Runtime.h"
#include "utils/convert.h"

using namespace JS;


void reportError(JSContext *cx, const char *message, JSErrorReport *report) {
    fprintf(stderr, "%s:%u:%s\n", report->filename ? report->filename : "[no filename]", (unsigned int) report->lineno, message);
}
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

    LOG("[PyJS_Context_eval] start\n");
    JS_BeginRequest(cx->cx);

    RootedValue rval(cx->cx);
    LOG("[PyJS_Context_eval] get global %p\n", cx->global);
    RootedObject global(cx->cx, cx->global);

    LOG("[PyJS_Context_eval] create compartment\n");
    JSAutoCompartment ac(cx->cx, global);
    OwningCompileOptions opts(cx->cx);
    opts.setVersion(JSVERSION_1_8);

    Evaluate(cx->cx, global, opts, code, strlen(code), &rval);

    JS_EndRequest(cx->cx);
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

        JS_BeginRequest(self->cx);
        CompartmentOptions opts;
        opts.setInvisibleToDebugger(true);

        self->global = JS_NewGlobalObject(self->cx, &global_class, nullptr, DontFireOnNewGlobalHook, opts);
        RootedObject global(self->cx, self->global);
        JS_SetErrorReporter(self->cx, reportError);

        LOG("[PyJS_Context_newfunc] global %p\n", self->global);
        JSAutoCompartment ac(self->cx, global);
        bool done = JS_InitStandardClasses(self->cx, global);
        LOG("[PyJS_Context_newfunc] global is populated %d\n", done);
        JS_EndRequest(self->cx);
        return (PyObject *)self;
    })
};
