import cv2
from deepface import DeepFace
import os

#Faz uma listagem dos arquivos no diretório
arquivos = os.listdir()

for arquivo in arquivos:
  if "jpg" in arquivo:
    #Ler a Imagem
    imagem = cv2.imread(arquivo)

    #Passar para o DeepFace
    resultado = DeepFace.analyze(imagem, actions=("age", "emotion"))

    #Resultado da análise
    print(resultado)