from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = add(a, b)

    return str(solution)
    
@app.route('/sub')
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = sub(a, b)

    return str(solution)

@app.route('/mult')
def mult_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = mult(a, b)

@app.route('/div')
def div_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    solution = div(a, b)

