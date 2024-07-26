from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
  return """<html><body><h1>welcome</h1></body></html>"""

@app.route('/welcome/home')
def say_wel_home():
  return """<html><body><h1>welcome home</h1></body></html>"""

@app.route('/welcome/back')
def say_wel_back():
  return """<html><body><h1>welcome back</h1></body></html>"""