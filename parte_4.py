from bottle import run, route, jinja2_view, request, response

@route('/<area>')
@jinja2_view('paginas/index.html')
def index(area):
    return dict(nome=area)

run(port=8080)