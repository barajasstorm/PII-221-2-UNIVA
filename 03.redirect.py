from bottle import run, route, redirect

@route('/')
def index():
    return "Running bottle with Python on UNIVA PII"




@route('/restricted')
def restricted():
    print("Using restricted method")
    redirect('/')

run(host='localhost', port=3001, debug=True, reloader=True)