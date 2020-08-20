'''
Faça um algoritimo que atraves da digitacao pelo teclado,
armazene em uma lista varias marcas de automoveis.

lista_de_marcas
[elemento01, elemento02, GM, VM, JEEP]
    0   1   2   3   4

0 [FIAT]
1 [GM]
2 [FORD]
3 [VW]
4 [JEEP]


'''
lista_de_marcas =[]

while True:
    escolha = input(''' Menu
    0- Finalizar o programa
    1- Cadastrar as marcas
    2- Listar as marcas cadastradas
    3- Alterar alguma marca digitada erradamente
    4- Excluir uma marca da lista
Escolha:  ''')

    if escolha == '0':
        break

    elif escolha == '1':
        nova_marca = input('...Digite a nova marca: ').upper()
        if nova_marca not in lista_de_marcas:
            lista_de_marcas.append(nova_marca)
        else:
            input('---ERRO. Marca já cadastrada. [ENTER] Continua.')

    elif escolha =='2':
        for marca in lista_de_marcas:
            print(marca)

    elif escolha == '3':

        marca_errada = input('...Digite a marca a ser alterada: ').upper()

        if marca_errada in lista_de_marcas:
            indice = lista_de_marcas.index(marca_errada)
            nova_marca = input ('....Digite a nova marca: ').upper()

            if nova_marca not in lista_de_marcas:
                lista_de_marcas[indice] = nova_marca
            else:
                input('---ERRO. Marca já cadastrada. [ENTER] Continua.')
        else:
            input('---ERRO. Marca não cadastrada. [ENTER] Continua.')

    elif escolha == '4':
        marca = input('...Digite a marca a ser excluída: ').upper()
        if marca in lista_de_marcas:
            lista_de_marcas.remove(marca)
        else:
            input('---ERRO. Marca não encontrada. [ENTER] Continua.')