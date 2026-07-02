# QUICKSORT NAIVE (NÃO IN PLACE)    

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


lista = [8, 6, 4, 1, 3, 2, 7, 5]
print(quick_sort(lista))









def quick_sort_primeiro_pivo(lista):
    # CASO BASE: Listas com 0 ou 1 elemento já estão ordenadas
    if len(lista) <= 1:
        return lista

    # 1. ESCOLHA DO PIVÔ (Usando o primeiro elemento)
    pivo = lista[0]

    # 2. PARTIÇÃO / DIVIDIR (Ignorando o primeiro elemento [1:])
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    # 3. CONQUISTAR E COMBINAR
    return quick_sort_primeiro_pivo(menores) + [pivo] + quick_sort_primeiro_pivo(maiores)