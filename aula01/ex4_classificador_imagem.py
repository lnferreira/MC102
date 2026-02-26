from transformers import pipeline
from PIL import Image

# 1. Carregar a "IA de visão" (modelo pré-treinado)
classificador = pipeline("image-classification", model="google/vit-base-patch16-224")

# 2. Abrir uma imagem (pode ser um arquivo local ou URL)
imagem = Image.open("../data/img/dog.jpg")

# 3. Pedir para a IA classificar
resultados = classificador(imagem)

# 4. Mostrar o que ela viu
for res in resultados:
    print(f"Eu vi um(a): {res['label']} (Confiança: {res['score']:.2%})")