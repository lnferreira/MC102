texto = input("Entre com uma palavra ou frase: ")
texto = texto.replace(" ", "")
texto = texto.lower()
if texto == texto[::-1]:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")
