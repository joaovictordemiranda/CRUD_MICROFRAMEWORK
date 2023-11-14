from bottle import run, route, jinja2_view, request, response

@route('/<area>')
@jinja2_view('paginas/index.html')
def index(area):
    return dict(nome=area)


@route('/user', method='GET')
@jinja2_view('paginas/user.html')
def user():
    links = ['home', 'about', 'contact']

    return dict(links=links)

@route('/user', method='POST')
@jinja2_view('paginas/user.html')
def user_post():
    username = request.forms.get('username')
    password = request.forms.get('password')

    if username == 'joao' and password == 'senha' or \
    request.get_cookie('user') == 'joao':
        
        response.set_cookie('user', 'joao')
        links = ['home', 'user_space', 'help', 'metrics']

        return dict(string='você esta Logado !', links=links)
    else:
        response.set_cookie('user', 'None')
        links = ['home', 'about', 'contact', 'logout']
        return dict(string='error, você não esta Logado', links=links)

run(port=8080)