# Aula 3 - Exercício 4
#
# Escreva um programa que calcule as raízes de uma equação de
# segundo grau. O seu programa deve receber três números a, b e c,
# sendo que a equação é definida como ax2 + bx + c = 0. O seu
# programa também deve tratar o caso em que a = 0.


a = float(input("Entre com o coeficiente a: "))
b = float(input("Entre com o coeficiente b: "))
c = float(input("Entre com o coeficiente c: "))

if a == 0:  # equação do primeiro grau
    if b == 0:
        print("Não existe raiz.")
    else:
        raiz = -c / b
        print("A raiz é:", raiz)
else:  # equação do segundo grau
    delta = (b**2) - (4 * a * c)
    if delta < 0:
        print("Não existem raízes reais.")
    elif delta > 0:
        raiz1 = (-b + delta ** (1 / 2)) / (2 * a)
        raiz2 = (-b - delta ** (1 / 2)) / (2 * a)
        print("As raízes são:", raiz1, "e", raiz2)
    else:
        raiz = -b / (2 * a)
        print("A raiz é:", raiz)
