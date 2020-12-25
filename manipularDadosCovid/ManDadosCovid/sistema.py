import interface
import arquivo
import classes
from time import sleep
 
#Ler os Arquivos txt.
arquivo.carregarArqEst()
arquivo.carregarArqCid()

#Funcoes
def cadastroDeEstado():
    interface.cabecalho('Novo Estado')
    est = classes.Estado(input('Estado: '),input('Sigla: '))
    a = False #bandeira
    for estado in arquivo.lst_estado:
        if estado.getNomeEstado() == est.getNomeEstado():
            print('\033[31mOpção inválida. Estado já cadastrado!\033[m')
            a = True
    if not a:
        arquivo.lst_estado.append(est)

def cadastroDeCidade():
    interface.cabecalho('Nova Cidade')
    cid = classes.Cidade(input('Cidade: '),interface.leiaInt('Quantidade de casos: '),input('Estado(Sigla): '))
    a = False 
    for cidade in arquivo.lst_cidade:
        if cidade.getCidade() == cid.getCidade():
            print('\033[31mOpção inválida. Cidade já cadastrada!\033[m')
            a = True
    if not a:
        arquivo.lst_cidade.append(cid)

def relatorioEstado():
    print('=-=-=-=-=- Relatório dos Estados:\n')
    for estado in arquivo.lst_estado:
        print(estado.retornaAtributos())

def relatorioCidade():
    print('=-=-=-=-=- Relatório das Cidades:\n')
    for cidade in arquivo.lst_cidade:
        print(cidade.retornaAtributos())


def atualizacaoCasos():
    print('=-=-=-=-=- Atualização de casos:\n')
    for cidade in arquivo.lst_cidade:
        print(cidade.retornaAtributos())
    cidadeEscolhida = input("Escolha uma das cidades: ").upper()
    a = False 
    for cidade in arquivo.lst_cidade:
        if cidade.getCidade() == cidadeEscolhida:
            cidade.atualizaCasos(int(input("Digite a quantidade atualizada de casos: ")))
            soma = 0
            for sigla in arquivo.lst_estado:
                if sigla.getSigla() == cidade.getEstado():
                    soma = soma +  cidade.getCasos()
                    sigla.atualizarCasos(soma)
        a = True
        if not a:
            print('\033[31mOpção inválida. Cidade não consta no sistema!\033[m')
    

#Menu
while True:
    resposta = interface.menu(['Finalizar o Programa', 'Cadastrar Estados', 'Cadastrar Cidades', 'Relatório de Estados', 'Relatório de Cidades', 'Atualizar números de casos'])
    if resposta == 1:
        interface.cabecalho('Saindo do Sistema.....Até logo e lave as mãos!')
        break
    elif resposta == 2:
        cadastroDeEstado()
        
    elif resposta == 3:
        cadastroDeCidade()

    elif resposta == 4:
        relatorioEstado()
        
    elif resposta == 5:
        relatorioCidade()

    elif resposta == 6:
        atualizacaoCasos()

    else:
        print('\033[31mOpção inválida. Digite novamente!\033[m')
    sleep(2)
