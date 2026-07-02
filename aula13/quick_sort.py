def quick_sort(lista):
    # CASO BASE
    if len(lista) <= 1:
        return lista

    # 1. ESCOLHA DO PIVÔ (Usando o último elemento)
    pivo = lista[-1]

    # 2. DIVIDIR
    menores = [x for x in lista[:-1] if x <= pivo]
    maiores = [x for x in lista[:-1] if x > pivo]

    # 3. CONQUISTAR E COMBINAR
    # Recursão nas duas metades + Pivô no meio
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


def quick_sort_inplace(lista, inicio, fim):
    # CASO BASE
    if inicio >= fim:
        return
    
    # 1. ESCOLHA DO PIVÔ (Usando o último elemento)
    pivo = lista[fim]
    i = inicio - 1
    
    # 2. DIVIDIR
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i+1], lista[fim] = lista[fim], lista[i+1]

    # 3. CONQUISTAR E COMBINAR
    # Recursão nas duas metades    
    quick_sort_inplace(lista, inicio, i)
    quick_sort_inplace(lista, i+2, fim)


lista = [3, 6, 8, 10, 1, 2, 1]
print(quick_sort(lista))