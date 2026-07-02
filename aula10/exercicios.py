# Exercício 1:
def le_matriz():
    M = []
    while True:
        temp = input().split()
        if temp == []:
            return M
        linha = []
        for i in temp:
            linha.append(int(i))
        M.append(linha)
    return M


# Exercício 2:
def dimensoes(M):
    linhas = len(M)
    colunas = len(M[0])
    for i in range(1, linhas):
        if len(M[i]) != colunas:
            return (-1, -1)
    return (linhas, colunas)


# Exercício 3:
def imprime_matriz(M):
    linhas, colunas = dimensoes(M)
    for i in range(linhas):
        for j in range(colunas):
            print(M[i][j], end=" ")
        print()


# Exercício 4:
def transposta(M):
    T = []
    linhas, colunas = dimensoes(M)
    for j in range(colunas):
        linha = []
        for i in range(
            linhas
        ):  # percorre as linhas para pegar os elementos da coluna j
            linha.append(M[i][j])
        T.append(linha)
    return T


# Exercício 5:
def soma(A, B):
    C = []
    dim_a = dimensoes(A)
    dim_b = dimensoes(B)
    if dim_a == dim_b:
        linhas, colunas = dim_a
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                linha.append(A[i][j] + B[i][j])
            C.append(linha)
    return C


M1 = le_matriz()
M1_dimensoes = dimensoes(M1)
print(f"Dimensões: {M1_dimensoes}")
imprime_matriz(M1)
