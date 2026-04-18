import os

restaurantes = ['Pizzaria do Bilbão', 
                'Hamburgueria do Paçoca', 
                'Sushi Bar da Lola', 
                'Churrascaria da Josie', 
                'Restaurante Vegetariano da Fefê']


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
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('clear')
    print('Finalizando o app\n')

def opcao_invalida():
    os.system('clear')
    print('Opção inválida\n')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()    

def cadastrar_novo_restaurante():
    #pass
    os.system('clear')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    input('\nDigite uma tecla para voltar ao menu principal\n')
    main()

def listar_restaurantes():
    os.system('clear')
    print('Listagem de restaurantes')
    print('------------------------\n')
    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado\n')
    else:
        for restaurante in restaurantes:
            print(f'- {restaurante}\n')
    input('Digite uma tecla para voltar ao menu principal\n')
    main()


def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))    
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
        # if opcao_escolhida == 1:
        #     print('Cadastrar restaurante')
        # elif opcao_escolhida == 2:
        #     print('Listar restaurantes')
        # elif opcao_escolhida == 3:
        #     print('Ativar restaurante')
        # elif opcao_escolhida == 4:
        #     finalizar_app()
        # else:
        #     print('Opção inválida')
    except:
        opcao_invalida()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()


