from flask import Flask, render_template, request, redirect

class Usuario:
    def __init__(self, nome, email, usuario, senha):
        self.nome = nome
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def novousuario(self):
        self.nome = request.form.get('nome')
        self.email = request.form.get('email')
        self.usuario = request.form.get('usuario')
        self.senha = request.form.get('senha')
        print(self.nome, self.email, self.usuario, self.senha)


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

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    print(nome, email, usuario, senha)


    return render_template('login.html')




app.run()