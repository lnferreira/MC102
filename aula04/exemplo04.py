dividendo = int(input("Entre com o dividendo : "))
divisor = int(input("Entre com o divisor: "))

quociente = 0

while dividendo >= divisor:
    dividendo = dividendo - divisor
    quociente = quociente + 1

print(" Quociente :", quociente)
print("Resto:", dividendo)
