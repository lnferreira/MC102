# Importa a biblioteca turtle para desenhar
import turtle

# Cria um objeto Turtle (a "caneta" para desenhar)
t = turtle.Turtle()

# Define a velocidade do desenho para a mais rápida
t.speed(0) 

# Define a cor de fundo da tela para preto
turtle.bgcolor("black")

# Define a cor da caneta para ciano
t.color("cyan")

# Loop para desenhar a espiral
for i in range(100):
    # Move a tartaruga para frente, aumentando a distância a cada passo
    t.forward(i * 3)
    # Gira a tartaruga em 91 graus para a esquerda, criando o efeito de espiral
    t.left(91)

# Mantém a janela aberta até que seja fechada manualmente
turtle.done()