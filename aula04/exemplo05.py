base = float(input("Base: "))
expoente = int(input("Expoente : "))

resultado = 1
i = 1

while i <= expoente:
    resultado = resultado * base
    i = i + 1

print(resultado)
