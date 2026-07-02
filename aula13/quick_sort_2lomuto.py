# QUICKSORT LOMUTO (IN PLACE)

def particao(lista, inicio, fim):
    # Escolhemos o último elemento como o pivô
    pivo = lista[fim]
    # Posição que o pivô ficará
    i = inicio - 1  
    # Percorre a lista ate o penultimo elemento
    for j in range(inicio, fim):
        # Se o elemento atual for menor ou igual ao pivô
        if lista[j] <= pivo:
            i += 1
            # Faz a troca direta (swap) na memória
            lista[i], lista[j] = lista[j], lista[i]
    # Coloca o pivô no seu lugar correto (logo após o menor elemento)
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1


def quick_sort(lista, inicio, fim):
    if inicio < fim:
        # Ponto de divisão onde o pivô já está no lugar certo
        p = particao(lista, inicio, fim)
        # Chamadas recursivas para as duas metades
        quick_sort(lista, inicio, p - 1)  # Metade esquerda
        quick_sort(lista, p + 1, fim)  # Metade direita


lista = [8, 6, 4, 1, 3, 2, 7, 5]
quick_sort(lista, 0, len(lista) - 1)
print(lista)