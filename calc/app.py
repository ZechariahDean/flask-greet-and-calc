# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def do_add():
  num = add(int(request.args["a"]), int(request.args["b"]))
  return f"<html><body><h1>{num}</h1></body></html>"

@app.route("/sub")
def do_sub():
  num = sub(int(request.args["a"]), int(request.args["b"]))
  return f"<html><body><h1>{num}</h1></body></html>"

@app.route("/mult")
def do_mult():
  num = mult(int(request.args["a"]), int(request.args["b"]))
  return f"<html><body><h1>{num}</h1></body></html>"

@app.route("/div")
def do_div():
  num = div(int(request.args["a"]), int(request.args["b"]))
  return f"<html><body><h1>{num}</h1></body></html>"

operations = {
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div
}
@app.route("/math/<operation>")
def do_operation(operation):
  num = operations[operation](int(request.args["a"]), int(request.args["b"]))
  return f"<h1>{num}</h1>"