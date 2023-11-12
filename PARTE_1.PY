"""
Uma breve Introdução sobre rotas

Estaticas & dinâmicas
"""
from bottle import run, route

@route('/')
def index():
    return '<h1>Olá, Mundo de Python</h1>'

@route('/<pessoa>')
def index(pessoa):
    return '<h1>Perfil {}</h1>'.format(pessoa)


run(port=8080)