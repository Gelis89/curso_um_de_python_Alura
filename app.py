#importando biblioteca
import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
    """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    #limpa o console
    os.system('cls')
    print('encerrando app\n')

def opcao_invalida():
    print('Opcção invalida\n')
    input('digite um numero para opção principal: ')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('cadastro de novos restaurante\n')
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar: ')
    #adicionar a lista
    restaurantes.append(nome_do_restaurante)
    print(f'o restaurante{nome_do_restaurante} foi cadastrado com sucesso\n')
    input('\ndigite uma tecla para para voltar ao menu principal')
    main()

def listar_restaurantes():
    os.system('cls')
    print('listando os restaurantes\n')
    #usando for in - para cada restaurante na lista restaurante 
    for restaurante in restaurantes:
        print(f'.{restaurante}')
        
    input('\ndigite uma tecla para para voltar ao menu principal')
    main()

def escolher_opcao():
    #tentar executar, caso não funcione ele exibe o except
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()    
        elif opcao_escolhida == 3:
            print('3. Ativar restaurante')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

#definindo como aquivo main(principal)
if __name__ == '__main__':
    main()
