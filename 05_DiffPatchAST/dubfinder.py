from argparse import ArgumentParser
from importlib import import_module
import inspect

parser = ArgumentParser()
parser.add_argument("module", type=str, nargs='+')
args = parser.parse_args()

def get_functions(obj, prefix):
    if not obj:
        return []
    functions = [(prefix + '.' + f[0], f[1]) for f in inspect.getmembers(obj, inspect.isfunction)]
    classes = inspect.getmembers(obj, inspect.isclass)
    for cls in classes:
        if not cls[0].startswith('__'):
            mem_functions = get_functions(cls[1], prefix + '.' + cls[0])
            functions += mem_functions
    return functions

functions = []
for module in args.module:
    mod = import_module(module)
    functions += get_functions(mod, module)
