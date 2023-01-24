from flask import Flask, render_template, request, redirect

class Usuario:
    def __init__(self, nome, email, usuario, senha):
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def cadastrar(self, nome, email, usuario, senha):
        pass

cadastrado_usuario = 'ruan'
cadastrado_senha = '1234'

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/esqueciasenha')
def esqueciasenha():
    return render_template('esqueciasenha.html')

@app.route('/autenticar', methods=['POST'])
def index():
    name = request.form.get('usuario')
    senha = request.form.get('senha')
    print(name, senha)

    if name == cadastrado_usuario and senha == cadastrado_senha:
        return render_template('index.html')
    else:
        print('Senha invalida')
        return render_template('login.html')


app.run()