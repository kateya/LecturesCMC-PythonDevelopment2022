from argparse import ArgumentParser
from importlib import import_module
from textwrap import dedent
from difflib import SequenceMatcher
import inspect
import ast

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

prep_functions = {}

for func in functions:
    src = inspect.getsource(func[1])
    if src.startswith(" "):
        src = dedent(src)
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if hasattr(node, 'name'):
            node.name = '_'
        if hasattr(node, 'id'):
            node.id = '_'
        if hasattr(node, 'arg'):
            node.arg = '_'
        if hasattr(node, 'attr'):
            node.attr = '_'
    prep = ast.unparse(tree)
    prep_functions[func[0]] = prep

result = {}

for f, p in prep_functions.items():
    max = 0.0
    fname = ''
    for fm, pm in prep_functions.items():
        if fm != f:
            r = SequenceMatcher(None, p, pm).ratio()
            if r > max:
                max = r
                fname = fm
    if max > 0.95:
        if result.get(fname) and result[fname] == f:
            continue
        result[f] = fname
        print(*sorted([f, fname]))
