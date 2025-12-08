#Início da Conexão com o SGBD
from operacoesbd import *

#Verificar antes se a escolha é válida ou não
escolhaRange = range(7)
opcaoEscolhida = None

#Listagem das manifestações
def listagemManifestacao(conexao):

    consulta = 'SELECT * FROM Manifestacoes'
    listarManifestacao = listarBancoDados(conexao, consulta)

    if len(listarManifestacao) == 0:
            print('\nNão há nenhuma manifestação disponível!')
    else:
        for manifestacao in listarManifestacao:
            print('\nCódigo: {}\nManifestação: {}'.format(manifestacao[0], manifestacao[1]))


#Adicionar manifestação
def addManifestacao(conexao):

    consulta = 'INSERT INTO Manifestacoes (manifestacao) values (%s)'
    manifestacao = input('\nDigite sua manifestação: ').strip().capitalize()

    if len(manifestacao) == 0:
        print('\nA manifestação não pode ser vazia!')
    else:
        dados = [manifestacao]

        codigoNovaManifestacao = insertNoBancoDados(conexao, consulta, dados)
        print('\nManifestação cadastrada com sucesso! Seu código é: {}.'.format(codigoNovaManifestacao))


#Procurar manifestação código
def searchManifestacao(conexao):

    consulta = 'SELECT * FROM Manifestacoes'
    listarManifestacao = listarBancoDados(conexao, consulta)

    if len(listarManifestacao) == 0:
            print('\nNão há nenhuma manifestação disponível para pesquisar!')

    else:
        try:
            pesquisarCodigo = int(input('\nDigite o código da manifestação desejada: '))
            consulta = 'SELECT * FROM Manifestacoes where codigo = %s'
            dados = [pesquisarCodigo]
            listarManifestacao = listarBancoDados(conexao, consulta, dados)

            if not listarManifestacao:
                    print('\nNão há nenhuma manifestação com esse código.')
            else:
                 for manifestacao in listarManifestacao:
                    print('\nCódigo: {}\nManifestação: {}'.format(manifestacao[0], manifestacao[1]))

        except ValueError:
            print('\nInsira um código válido!')


#Excluir manifestação pelo código
def excluirManifestacao(conexao):

    consulta = 'SELECT * FROM Manifestacoes'
    listarManifestacao = listarBancoDados(conexao, consulta)

    if len(listarManifestacao) == 0:
            print('\nNão há nenhuma manifestação disponível para excluir!')

    else:
        consulta = 'DELETE FROM Manifestacoes WHERE codigo = %s'
        try:
            removerManifestacao = int(input('\nDigite o código da manifestação para ser EXCLUÍDA: '))
            valores = [removerManifestacao]
            manifestacaoRemover = excluirBancoDados(conexao, consulta, valores)

            if not manifestacaoRemover:
                print('\nNão há nenhuma manifestação com esse código para ser removida.')
            else:
                    print('\nManifestação removida com sucesso!')

        except ValueError:
            print('\nInsira um código válido!')


#Exibir quantidade de manifestações
def quantidadeManifestacao(conexao):

    consulta = 'SELECT count(*) from Manifestacoes'
    listarManifestacao = listarBancoDados(conexao, consulta)

    exibirQuantidade = listarManifestacao[0][0]

    if not exibirQuantidade:
        print('\nNão há nenhuma manifestação registrada no sistema.')

    elif exibirQuantidade == 1:
        print('\nHá {} manifestação registrada no sistema.'.format(exibirQuantidade))

    else:
        print('\nHá {} manifestações registradas no sistema.'.format(exibirQuantidade))