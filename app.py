import os

restaurantes = [{'nome':'Praça',         'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza',    'ativo':True},
                {'nome':'Cantina',       'categoria':'Italiano', 'ativo':False}]

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
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu: ')
    main()

def opcao_invalida():
    os.system('clear')
    print('Opção inválida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha + '\n')

def cadastrar_novo_restaurante():
    '''Esta função faz o cadastro de um novo restaurante

    Inputs:
        - Nome_do_restaurante: str
        - Categoria: str
    Outputs:
        - Adiciona um novo restaurante à lista de restaurantes
    '''      
    #pass
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    '''
    Esta função lista os restaurantes cadastrados, mostrando nome, categoria e se estão ativos
    '''  
    exibir_subtitulo('Listagem de restaurantes')

    if len(restaurantes) == 0:
        print('Nenhum restaurante cadastrado\n')
    else:
        print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status \n')
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']
            categoria        = restaurante['categoria']
            ativo            = 'ativado' if restaurante['ativo'] else 'desativado'
            print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | Ativo: {ativo} \n')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    '''
    Esta função altera o estado do restaurante, ou seja, ativa ou desativa um restaurante cadastrado. 
    '''  
    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja ativar / desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'   
            print(mensagem)    

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''
    Esta função lê a opção escolhida pelo usuário e chama a função correspondente à opção escolhida.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))    
        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
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


