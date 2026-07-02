# Busca Binária Recursiva

def busca_binaria(lista, elemento, inicio, fim):
    if inicio > fim:
        return -1
    meio = (inicio + fim) // 2
    if lista[meio] == elemento:
        return meio
    elif lista[meio] > elemento:
        return busca_binaria(lista, elemento, inicio, meio - 1)
    else:
        return busca_binaria(lista, elemento, meio + 1, fim)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(busca_binaria(lista, 2, 0, len(lista) - 1))