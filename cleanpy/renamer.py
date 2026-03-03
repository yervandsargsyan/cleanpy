import ast
import re
import builtins
builtins = set(dir(builtins))

def to_snake_case(name: str) -> str:
    s1 = re.sub('(.)([A-Z][a-z] + )', '\\1_\\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', '\\1_\\2', s1)
    return s2.lower()

class RenameTransformer(ast.NodeTransformer):

    def visit__function_def(self, node):
        node.name = to_snake_case(node.name)
        self.generic_visit(node)
        return node

    def visit__class_def(self, node):
        node.name = to_snake_case(node.name)
        self.generic_visit(node)
        return node

    def visit__name(self, node):
        if node.id not in builtins:
            node.id = to_snake_case(node.id)
        return node