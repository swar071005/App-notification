from flask import Flask, request, jsonify, send_from_directory
import ast
import operator as op

app = Flask(__name__, static_folder='.', static_url_path='')

# Supported operators
ALLOWED_OPERATORS = {
    ast.Add:  op.add,
    ast.Sub:  op.sub,
    ast.Mult: op.mul,
    ast.Div:  op.truediv,
    ast.Pow:  op.pow,
    ast.USub: op.neg,
}

def safe_eval(node):
    """Recursively evaluate an AST node safely."""
    if isinstance(node, ast.Num):  # <number> (Python <3.8)
        return node.n
    if isinstance(node, ast.Constant):  # <number> (Python 3.8+)
        return node.value
    if isinstance(node, ast.BinOp):  # <left> op <right>
        left  = safe_eval(node.left)
        right = safe_eval(node.right)
        if type(node.op) in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[type(node.op)](left, right)
        else:
            raise ValueError(f"Operator {type(node.op)} not allowed")
    if isinstance(node, ast.UnaryOp):  # - <operand>
        if type(node.op) in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[type(node.op)](safe_eval(node.operand))
        else:
            raise ValueError(f"Unary operator {type(node.op)} not allowed")
    raise ValueError(f"Unsupported expression: {node!r}")

@app.route('/')
def index():
    # Serve the static HTML
    return send_from_directory('.', 'index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or {}
    expr = data.get('expression', '')
    try:
        # Parse expression into AST
        tree = ast.parse(expr, mode='eval')
        result = safe_eval(tree.body)
        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)
