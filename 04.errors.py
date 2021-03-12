from bottle import run, route, error, abort

@error(400)
def bad_request(error):
    return "400 Bad Request"

@error(401)
def unauthorized(error):
    return "401 Unauthorized"


@route('/')
def index():
    return "Welcome to Bottle Python Web Framework"



@route('/bad_request_route')
def bad_request_route():
    abort(400)    

@route('/unauthorized')
def unauthorized():
    abort(401)      

run(host='localhost', port=3002, debug= True, reloader= True)

