from bottle import run, route, request, response

@route('/')
def index():
    if request.get_cookie('visited'):
        return '<h1>Olá, Mundo de Python</h1>'
    response.set_cookie('visited', 'yes')
    return 'Olá, é um prazer conhecer voce'

run(port=8080)
