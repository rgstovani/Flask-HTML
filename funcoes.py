import sqlite3
from hashlib import sha256


def cria_bd():
    conn = sqlite3.connect('dados_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    NOME TEXT NOT NULL,
    EMAIL TEXT NOT NULL,
    USUARIO TEXT NOT NULL UNIQUE,
    SENHA TEXT NOT NULL);
    ''')
    conn.commit()
    conn.close()


def adiciona_usuario_bd(nome, email, usuario, senha):
    cria_bd()
    hashsenha = sha256(senha.encode()).hexdigest()
    hashusuario = sha256(usuario.encode()).hexdigest()
    try:
        conn = sqlite3.connect('dados_usuarios.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO users VALUES (:NOME, :EMAIL, :USUARIO, :SENHA)
        ''', {"NOME": nome, "EMAIL": email, "USUARIO": hashusuario, "SENHA": hashsenha})
        conn.commit()
        conn.close()
    except sqlite3.Error:
        return False



def teste_login(usuario, senha):
    testeusuario = sha256(usuario.encode()).hexdigest()
    testesenha = sha256(senha.encode()).hexdigest()

    conn = sqlite3.connect('dados_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE (USUARIO=? AND SENHA=?)
    ''', (testeusuario, testesenha))
    teste_login = cursor.fetchone()
    conn.commit()
    conn.close()

    if teste_login is None:
        return False
    if (testeusuario in teste_login) and (testesenha in teste_login):
        return True
    else:
        return False


def esquecisenha_bd(email, usuario):
    hashusuario = sha256(usuario.encode()).hexdigest()

    conn = sqlite3.connect('dados_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM users WHERE (EMAIL=? AND USUARIO=?)
    ''', (email, hashusuario))
    teste_esqueci_senha = cursor.fetchone()
    conn.commit()
    conn.close()

    if teste_esqueci_senha is None:
        return False
    if (email in teste_esqueci_senha) and (hashusuario in teste_esqueci_senha):
        return True
    else:
        return False


def altera_senha_bd(usuario, senha): # Aqui falta guardar o nome do usuario
    hashsenha = sha256(senha.encode()).hexdigest()
    conn = sqlite3.connect('dados_usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE users SET SENHA = ? WHERE USUARIO = ?
    ''', (hashsenha, usuario))
    conn.commit()
    conn.close()
