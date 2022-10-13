# Primeiro menu de interface do programa

from time import sleep

def linha(tamanho=90):
    print('='*tamanho)


def cabecalho():
    linha()
    print('Extraindo Dados Da Api Do Youtube')
    linha()


def menu_inicial():
    cabecalho()
    print('1 - Inserir o id do video ou a playlist que desaja analisar os dados \n'
          '2 - Sair do sistema')
    opcao: int = int(input('Informe sua opção: '))
    menu_secundario(opcao)
    pass


def menu_secundario(opcao):
    cabecalho()
    if opcao == 1:
        pass
    elif opcao == 2:
        exit()
    else:
        print('Opção inválida')
        sleep(1)
        menu_inicial()

