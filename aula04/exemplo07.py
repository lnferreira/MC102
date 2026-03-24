n = 0
OK = True

while OK:
    x = int(input("Entre com um número inteiro positivo : "))
    if x > 0:
        n = n + 1
    else:
        OK = False

print("Quantidade de números positivos fornecidos :", n)
