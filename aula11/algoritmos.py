def busca_sequencial(lista, chave):
    for i in range(len(lista)):
        if lista[i] == chave:
            return i
    return -1


def busca_binaria(lista, chave):
    baixo, alto = 0, len(lista) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista[meio] == chave:
            return meio
        elif lista[meio] < chave:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

elemento
