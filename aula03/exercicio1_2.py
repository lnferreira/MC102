a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))
if (a <= b) and (a <= c):
    print(a)
elif b <= c:
    print(b)
else:
    print(c)
