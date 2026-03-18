# Aula 3 - Exercício 5
#
# Escreva um programa que simula o jogo conhecido como “Pedra,
# Papel e Tesoura” de um jogador A contra um jogador B. O
# programa deve ler a escolha do jogador A e a escolha do jogador B.
# Por fim, o programa deve indicar quem foi o vencedor.


print("Pedra = 0")
print("Papel = 1")
print("Tesoura = 2")

jogadorA = int(input("Entre com a primeira escolha: "))
jogadorB = int(input("Entre com a segunda escolha: "))

resultado = (jogadorA - jogadorB) % 3

if resultado == 1:
    print("O jogador A ganhou")
elif resultado == 2:
    print("O jogador B ganhou")
else:
    print("Empate")
