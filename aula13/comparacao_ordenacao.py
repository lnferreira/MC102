import random
import time

def bubble_sort(lista):
    """
    Ordenação por flutuação (Bubble Sort) - O(n^2)
    Modifica a lista recebida in-place e a retorna.
    """
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        # Se nenhuma troca ocorreu nesta passada, a lista já está ordenada
        if not trocou:
            break
    return lista

def selection_sort(lista):
    """
    Ordenação por seleção (Selection Sort) - O(n^2)
    Modifica a lista recebida in-place e a retorna.
    """
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Troca o menor elemento encontrado com o elemento na posição i
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    """
    Ordenação por inserção (Insertion Sort) - O(n^2)
    Modifica a lista recebida in-place e a retorna.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        # Move os elementos da lista que são maiores que a chave para uma posição à frente
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

def merge_sort(lista):
    """
    Ordenação por intercalação (Merge Sort) - O(n log n)
    Retorna uma nova lista ordenada.
    """
    if len(lista) <= 1:
        return lista
    
    # Dividir
    meio = len(lista) // 2
    metade_esquerda = lista[:meio]
    metade_direita = lista[meio:]
    
    # Conquistar (Recursão)
    esquerda_ordenada = merge_sort(metade_esquerda)
    direita_ordenada = merge_sort(metade_direita)
    
    # Combinar
    return merge(esquerda_ordenada, direita_ordenada)

def merge(esquerda, direita):
    """Auxiliar para o Merge Sort: intercala duas listas ordenadas."""
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort_naive(lista):
    """
    Quick Sort Naive - O(n log n) no caso médio
    Usa listas auxiliares (não in-place).
    """
    if len(lista) <= 1:
        return lista
    
    pivo = lista[-1]
    menores = [x for x in lista[:-1] if x <= pivo]
    maiores = [x for x in lista[:-1] if x > pivo]
    
    return quick_sort_naive(menores) + [pivo] + quick_sort_naive(maiores)

def quick_sort_lomuto(lista):
    """
    Quick Sort Lomuto - O(n log n) no caso médio
    Ordena in-place usando a partição de Lomuto com pivô central.
    """
    lista_copia = lista.copy()
    _quick_sort_recursivo(lista_copia, 0, len(lista_copia) - 1)
    return lista_copia

def _quick_sort_recursivo(lista, inicio, fim):
    if inicio < fim:
        # Partição
        p = _particao_lomuto(lista, inicio, fim)
        # Recursão nas duas metades
        _quick_sort_recursivo(lista, inicio, p - 1)
        _quick_sort_recursivo(lista, p + 1, fim)

def _particao_lomuto(lista, inicio, fim):
    # Escolha do pivô no meio para mitigar o pior caso (vetor já ordenado)
    meio = (inicio + fim) // 2
    lista[meio], lista[fim] = lista[fim], lista[meio]
    pivo = lista[fim]
    
    i = inicio - 1
    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
            
    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

def benchmark():
    tamanho = 15000
    print(f"Gerando vetor aleatório de tamanho {tamanho}...")
    vetor_original = [random.randint(1, 100000) for _ in range(tamanho)]
    
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort Naive": quick_sort_naive,
        "Quick Sort Lomuto": quick_sort_lomuto
    }
    
    print("\nIniciando testes de ordenação...")
    print("-" * 35)
    print(f"{'Algoritmo':<18} | {'Tempo (s)':<12}")
    print("-" * 35)
    
    for nome, alg in algoritmos.items():
        # Faz uma cópia para garantir que a ordenação seja justa e não reutilize a lista ordenada
        vetor_copia = vetor_original.copy()
        
        inicio = time.time()
        vetor_ordenado = alg(vetor_copia)
        fim = time.time()
        
        tempo_decorrido = fim - inicio
        print(f"{nome:<18} | {tempo_decorrido:10.5f} s")
        
    print("-" * 35)

if __name__ == "__main__":
    benchmark()
