from bottle import run, route

@route('/')
def index():
    return "Welcome to Bootle framework for Python Juan Barajas"

run(host='localhost', port=3000, debug=True, reLoader=True)