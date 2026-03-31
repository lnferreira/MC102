# Números Primos

# Escreva um programa que leia um número inteiro positivo (n > 1) e
# determine se ele é primo.
n = int(input("Digite um número inteiro positivo: "))
divisores = 0
for divisor in range(1, n + 1):
    if n % divisor == 0:
        divisores = divisores + 1
if divisores == 2:
    print("Primo")
else:
    print("Composto ")
