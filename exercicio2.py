import os

def limpar():
    #limpa o console
    os.system('cls')

numero_par = int(input('digite um numero: '))

if numero_par % 2 == 0:
    limpar()
    print('é um numero par')
else:
    print('numero impar')

numero_idade = int(input('digite sua idade: '))

if numero_idade <= 12:
    limpar()
    print('você é uma crianca')
elif numero_idade <= 18:
    print('você é adolecente')
else:
    print('você é adulto')

nome_usuario = input('digite seu nome de usuario: ')
numero_senha = int(input('digite sua senha '))

if len(nome_usuario) == numero_senha:
    limpar()
    print('passou')
else:
    ('falhou')






