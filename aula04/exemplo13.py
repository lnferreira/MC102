x = int(input("Digite um número: "))
for i in [2, 4, 7, 1, 0, 8, 9, 5]:
    if i == x:
        print("Elemento", i, "encontrado!")
        break
else:  # Só executa se o laço for concluído SEM encontrar o elemento
    print("O elemento", x, "não está na lista.")
