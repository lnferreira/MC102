# Importa as bibliotecas necessárias
# pyautogui: para automação de GUI (movimentar mouse, teclado, etc)
# webbrowser: para abrir o navegador de internet
# time: para adicionar pausas no programa
import pyautogui, webbrowser, time

# Pede para o usuário digitar o que ele quer buscar e armazena na variável texto_busca
texto_busca = input("Buscar: ")

# Abre o site do Google no navegador padrão
webbrowser.open("https://www.google.com")

# Espera 2 segundos para a página carregar
time.sleep(2) 

# Escreve o texto da busca na barra de pesquisa do Google
# O 'interval' é o tempo entre a digitação de cada caractere
pyautogui.write(texto_busca, interval=0.1)

# Pressiona a tecla "enter" para realizar a busca
pyautogui.press("enter")
