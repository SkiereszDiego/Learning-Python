import classes

def arquivoExiste(nome):
    try:
        a=open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #escreve o arq.txt e se por um acaso ele nao existir ele cria
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

arqEst = 'dadosEstados.txt'
arqCid = 'dadosCidades.txt'

if not arquivoExiste(arqEst):
    criarArquivo(arqEst)

if not arquivoExiste(arqCid):
    criarArquivo(arqCid)

lst_estado = []
lst_cidade = []

def carregarArqEst():
    try:
        a = open(arqEst, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in a:
            dado = linha.strip().split(';')
            dado[1] = dado[1].replace('\n', '')
            lst_estado.append(classes.Estado(*dado)) 

    finally: #dado certo ou dando errado ele e fechado
            a.close()

def carregarArqCid():
    try:
        b = open(arqCid, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        for linha in b:
            dado = linha.strip().split(';')
            dado[2] = dado[2].replace('\n', '')
            lst_cidade.append(classes.Cidade(dado[0],int(dado[1]),dado[2]))
    finally: #dado certo ou dando errado ele e fechado
            b.close()