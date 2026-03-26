x = int(input("Digite um número: "))
for i in [2, 4, 7, 1, 0, 8, 9, 5]:
    print("Verificando elemento", i)
    if i == x:
        print("Elemento", i, "encontrado!")
        break
