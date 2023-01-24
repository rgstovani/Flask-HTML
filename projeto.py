from funcoes import *
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    return render_template('login.html')


@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    return render_template('cadastro.html')


@app.route('/esqueciasenha', methods=['POST', 'GET'])
def esqueciasenha():
    return render_template('esqueciasenha.html')


@app.route('/autenticar', methods=['POST', 'GET'])
def autenticar_troca_senha():
    teste = esquecisenha_bd(request.form.get('email'), request.form.get('usuario'))

    if teste is True:
        return render_template('alterarsenha.html')
    else:
        return render_template('esqueciasenha.html')


@app.route('/alterarsenha', methods=['POST', 'GET'])
def alterarsenha():
    return render_template('alterarsenha.html')


# pagina intermediaria
@app.route('/autenticar', methods=['POST', 'GET'])
def index():
    login = teste_login(request.form.get('usuario'), request.form.get('senha'))

    if login is False:
        return render_template('login.html')
    if login is True:
        return render_template('index.html')


@app.route('/cadastrar', methods=['POST', 'GET'])
def cadastrar():
    adiciona_usuario_bd(request.form.get('nome'),
                        request.form.get('email'),
                        request.form.get('usuario'),
                        request.form.get('senha'))
    return render_template('login.html')


app.run()
