# Aula 3 - Exercício 5
#
# Escreva um programa que simula o jogo conhecido como “Pedra,
# Papel e Tesoura” de um jogador A contra um jogador B. O
# programa deve ler a escolha do jogador A e a escolha do jogador B.
# Por fim, o programa deve indicar quem foi o vencedor.

jogadorA = input("Entre com a primeira escolha: ")
jogadorB = input("Entre com a segunda escolha: ")

if jogadorA == "pedra":
    if jogadorB == "pedra":
        print("Empate")
    elif jogadorB == "tesoura":
        print("O jogador A ganhou")
    else:
        print("O jogador B ganhou")

elif jogadorA == "tesoura":
    if jogadorB == "pedra":
        print("O jogador B ganhou")
    elif jogadorB == "tesoura":
        print("Empate")
    else:
        print("O jogador A ganhou")

else:  # jogadorA == "papel"
    if jogadorB == "pedra":
        print("O jogador A ganhou")
    elif jogadorB == "tesoura":
        print("O jogador B ganhou")
    else:
        print("Empate")
