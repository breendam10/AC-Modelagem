from flask import Blueprint, render_template, request, jsonify
from functions.gauss_elimination import gauss_elimination

gauss_bp = Blueprint('gauss', __name__, template_folder='../static/html')

@gauss_bp.route('/', methods=['GET'])
def show_gauss_form():
    return render_template('gauss_elimination.html')

@gauss_bp.route('/', methods=['POST'])
def compute_gauss():
    try:
        A = request.form.get('A')
        b = request.form.get('b')
        import ast
        A = ast.literal_eval(A)
        b = ast.literal_eval(b)
        x = gauss_elimination(A, b)
        return jsonify({'solution': x})
    except Exception as e:
        return jsonify({'error': str(e)}), 400