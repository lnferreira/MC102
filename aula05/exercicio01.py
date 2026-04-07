# Escreva um programa que recebe como entrada um número inteiro
# positivo n. Em seguida, seu programa deve ler n números inteiros e
# adicioná-los em uma lista. Por fim, seu programa receberá um
# número inteiro x e deve verificar se x pertence ou não à lista.

n = int(input("Quantos números serão lidos? "))
lista = []
for i in range(n):
    lista.append(int(input()))
x = int(input("Qual o número a procurar? "))
if x in lista:
    print(x, "pertence à lista")
else:
    print(x, "não pertence à lista")
