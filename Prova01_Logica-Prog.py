
###################################################
#   Avaliação 1
# - Competências a serem avaliadas:
# . Saber desenvolver uma solução viável para o problema
# . Entender os comandos utilizados
# . Saber utilizar os comando corretamente

'''
Faça um algoritmo onde o usuário digite 2 números inteiros(n1 e n2).
Verifique se esses números estão entre 10 e 50 (inclusive).
Se estiverem neste intervalo e o primeiro for maior que o segundo,
    imprima em ordem crescente, todos os números que estiverem entre n1 e n2.
Caso os números estejam no intervalo pedido, e o segundo for maior que o primeiro,
    imprima em ordem decrescente todos os números do intervalo entre n1 e n2.

Caso um ou ambos números não estejam no intervalo pedido, mostre a seguinte mensagem:
"...Números fora do intervalo desejado.", e peça ao usuário digitá-los novamente.
obs.: o intervalo deve incluir os números digitados.

Neste código, você deverá utilizar 2 listas (lst_A e lst_B). Na lst_A, você deverá colocar todos os
números pares gerados no intervalo, e em lst_B, você deverá colocar todos os números cujo final(unidade)
seja 3 ou 4. Por fim, imprima as lista conforme o exemplo. Tente imprimir as listas conforme mostrado
no exemplo.

Exemplo:
Digite n1: 15
Digite n2: 33
33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15

lst_A:
[32][30][28][26][24][22][20][18][16]
lst_B:
[33][24][23]
'''

print ('********** Executando o Programa **********')

lista_A = []
lista_B = []
intervalo = []
lista_3_4 = [13, 14, 23, 24, 33, 34, 43, 44]

while True:
    
    n1 = int(input('Digite um numero inteiro: '))
    n2 = int(input('Digite o segundo numero inteiro: '))

    if (10 < n1 > 50 or 10 < n2 > 50):
        print('...numeros fora do intervalo desejado.')
    else:
        break

#Imprimir o intervalo, porem como fazer se o n1 for maior???, end='' é para imrpimir lado a lado
for i in range(n1, n2):
    intervalo.append(i)
    print(i, end = ' ')

#verifica se o numero é n1 é menor q n2 e é par. Ter resto 2 . Add na lista A
if n1 < n2:
    for x in range(n1+1,n2):
        print(x, end= ' ')
        if x % 2 == 0:
            lista_A.append(x)
                    
        #verifica se o numero é n2 é menor q n1 e é par. Ter resto 2. Add na lista A
else:
    for x in range(n1-n2):
        print(n1-x, end= ' ')
        if x % 2 == 0:
            lista_A.append(x)

#Usei a função set para realizar operações com conjuntos, porem fica desordenada. Ta dificil
s1= set(intervalo)  
s2 =set(lista_3_4)
lista_B = s1.intersection(s2) 
  
print("Lista A: \n", lista_A)
print("Lista B: \n",lista_B)
		
	
            






