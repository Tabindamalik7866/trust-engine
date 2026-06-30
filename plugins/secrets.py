import ast

class SecretsDetector(ast.NodeTransformer):
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name) and any(x in target.id.lower() for x in ['key', 'password']):
                if isinstance(node.value, ast.Constant):
                    print(f"[*] AUTO-FIXING: Replacing secret at line {node.lineno}")
                    # Change: api_key = "123" -> api_key = os.getenv("API_KEY")
                    node.value = ast.Call(
                        func=ast.Attribute(value=ast.Name(id='os', ctx=ast.Load()), attr='getenv', ctx=ast.Load()),
                        args=[ast.Constant(value=target.id.upper())], keywords=[]
                    )
        return node