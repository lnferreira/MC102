# Escreva um programa que, dada uma sequência de números inteiros
# (todos fornecidos na mesma linha, separados por espaços), imprima
# a média desses números.

numeros = [int(i) for i in input("Números: ").split()]
media = sum(numeros) / len(numeros)
print(f"Média: {media}")
