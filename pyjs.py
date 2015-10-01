import py_js as pyjs
import json

__all__ = ['Context']

class Context():
    def __init__(self):
        self.rt = pyjs.Runtime()
        self.cx = self.rt.Context()

    def eval(self, js):
        return self.cx.eval(js)

    def setGlobal(self, name, data):
        if not data:
            tmpl = "var %s=null" % name
        else:
            tmpl = "%s=JSON.parse('%s')" % (name, json.dumps(data))
        self.cx.eval(tmpl);
