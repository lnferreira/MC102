n = int(input("Entre com um número inteiro positivo : "))
fat = 1


while n > 1:
    fat = fat * n
    n = n - 1

print("Resultado :", fat)
