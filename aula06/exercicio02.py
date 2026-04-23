# Escreva um programa que, dada uma string representando um texto,
# imprima o número de palavras existentes. Observação: você deve
# remover os sinais de pontuação (“.”, “,”, “:”, “;”, “!” e “?”)
# antes de realizar a contagem das palavras.

texto = input("Texto: ")
pontuacao = [".", ",", ":", ";", "!", "?"]
for p in pontuacao:
    texto = texto.replace(p, " ")
palavras = texto.split()
print(f"Número de palavras: {len(palavras)}")
