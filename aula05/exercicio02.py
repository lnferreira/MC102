# Escreva um programa que leia números positivos e os armazene
# numa lista (até que um número não positivo seja fornecido). Por
# fim, seu programa receberá um número inteiro x e deve verificar se x
# pertence ou não à lista.

print("Entre com números positivos :")
lista = []
while True:
    p = int(input())
    if p <= 0:
        break
    lista.append(p)
x = int(input("Qual o número a procurar ? "))
if x in lista:
    print(x, "pertence à lista")
else:
    print(x, "não pertence à lista")
