#Sistema de cadastro de usuário e login
# 1. irá importar a biblioteca CSV

import csv

def cadastrar_usuario(nome, email, senha):
    with open('usuarios.csv','a', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow([nome, email, senha])
    print("Usuário cadastrado com sucesso!")

#verificar se o usuário já é cadastrado no sistema
def verificar_usuario(email, senha):
    with open('usuarios.csv', 'r') as arquivo_csv:
        reader = csv.reader(arquivo_csv)
        for row in reader:
            if row[1] == email and row[2] == senha:
                return True
    return False

def main():
    while True:
        print('1. Cadastrar Usuário')
        print('2. Entrar')
        print('3. Sair')
        escolha = input('Escolha uma opção: ')




