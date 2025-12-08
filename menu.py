from ouvidoria import *
from operacoesbd import criarConexao, encerrarConexao

conexao = criarConexao('localhost', 'root', 'SUA_SENHA', 'ouvidoriaxyz')


print('\nBem vindo(a) à Ouvidoria da Universidade XYZ! Temos as seguintes opções:')
print('\n1) Listar manifestações no sistema\n2) Adicionar manifestação\n3) Pesquisar manifestação por código\n4) Remover manifestação\n5) Exibir quantidade de manifestações \n6) Sair')


while True:
    try:
        opcaoEscolhida = int(input('\nSelecione a operação desejada: '))

        if opcaoEscolhida not in escolhaRange or opcaoEscolhida == 0:
            print('\nPor favor, selecione uma opção disponível.')

    except ValueError:
        (print('\nSelecione uma opção válida!'))
        opcaoEscolhida = None

    if opcaoEscolhida == 1:
        listagemManifestacao(conexao)

    elif opcaoEscolhida == 2:
        addManifestacao(conexao)

    elif opcaoEscolhida == 3:
        searchManifestacao(conexao)

    elif opcaoEscolhida == 4:
        excluirManifestacao(conexao)

    elif opcaoEscolhida == 5:
        quantidadeManifestacao(conexao)

    elif opcaoEscolhida == 6:
        break

encerrarConexao(conexao)

print('\nObrigado por utilizar nosso sistema!')
