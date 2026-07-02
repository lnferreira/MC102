def merge_sort(lista):
    # CASO BASE: 
    # Uma lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return lista

    # 1. DIVIDIR
    meio = len(lista) // 2
    # Fatia do início até o meio
    metade_esquerda = lista[:meio] 
    # Fatia do meio até o fim 
    metade_direita = lista[meio:]  

    # 2. CONQUISTAR (Chamadas Recursivas)
    esquerda_ordenada = merge_sort(metade_esquerda)
    direita_ordenada = merge_sort(metade_direita)

    # 3. COMBINAR
    return merge(esquerda_ordenada, direita_ordenada)


def merge(lista_esquerda, lista_direita):
    lista_unida = []
    i = 0  # Indice para a lista da esquerda
    j = 0  # Indice para a lista da direita

    # Compara os elementos de ambas as listas e insere o menor
    while i < len(lista_esquerda) and j < len(lista_direita):
        if lista_esquerda[i] < lista_direita[j]:
            lista_unida.append(lista_esquerda[i])
            i += 1
        else:
            lista_unida.append(lista_direita[j])
            j += 1

    # Se restaram elementos na esquerda, adiciona-os ao final
    while i < len(lista_esquerda):
        lista_unida.append(lista_esquerda[i])
        i += 1

    # Se restaram elementos na direita, adiciona-os ao final
    while j < len(lista_direita):
        lista_unida.append(lista_direita[j])
        j += 1

    return lista_unida

lista = []
while True:
    x = input("Digite um número: ")
    if x == "":
        break
    lista.append(int(x))

print(merge_sort(lista))


