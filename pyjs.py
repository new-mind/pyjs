import py_js as pyjs

__all__ = ['Context']

class Context():
    def __init__(self):
        self.rt = pyjs.Runtime()
        self.cx = self.rt.Context()

    def eval(self, js):
        return self.cx.eval(js)
