# Escreva um programa que, dada uma string texto e uma string
# palavra, ache todas as posições de ocorrência da palavra no
# texto. O seu programa deve desconsiderar se as letras são
# maiúsculas ou minúsculas.

texto = input("Entre com um texto: ")
palavra = input("Entre com uma palavra: ")
texto = texto.lower()
palavra = palavra.lower()
removido = 0
while palavra in texto:
    posicao = texto.find(palavra)
    print(f"Palavra encontrada na posição: {posicao + removido}")
    texto = texto[posicao + len(palavra) :]
    removido += posicao + len(palavra)
