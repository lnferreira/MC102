n = int(input("Entre com o tamanho dos catetos: "))
c = input("Entre com caractere a ser usado: ")

for i in range(1, n + 1):
    for j in range(i):
        print(c, end="")
    print()
