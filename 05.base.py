from bottle import run, route, template, view, static_file

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static/')

@route('/')
def home():
    return "Welcome to a Python framework"

@route('/index')
@view('index')
def index():
    #return "Reutrn Index"
    return dict(name = "Index")


@route('/about')
@view('about')
def about():
    #return "Reutrn Index"
    return dict(name = "about")

@route('/service')
@view('service')
def service():
    #return "Reutrn Index"
    return dict(name = "service")

@route('/contact')
@view('contact')
def contact():
    #return "Reutrn Index"
    return dict(name = "contact")




run(host="localhost", port=3000, debug=True, reloader=True)