# Importa a biblioteca de text-to-speech
import pyttsx3

# Pede ao usuário para digitar algo
text_to_speak = input("O que você quer que eu fale? \n")

# Inicializa o motor de TTS
engine = pyttsx3.init()

# Configurando a voz em PTBR no MacOS
engine.setProperty('voice', "com.apple.voice.compact.pt-BR.Luciana")

# Manda o motor falar o texto
engine.say(text_to_speak)

# Executa e espera a fala terminar
engine.runAndWait()
