from bottle import run, route, template, view

@route('/')
def index():
    return template("Welcome to {{ name }}), a Python framework", name = "Bottle v0.12.19")

@route('/home')
@view('home_template')
def home():
    return dict(name = "Bottle v0.12.19")

@route('/index')
@view('index2')
def index():
    return dict(index = "Home")

run(host="localhost", port=3000, debug=True, reloader=True)