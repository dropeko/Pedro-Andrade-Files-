#Gravador de tela do PC com Python
#Importando as bibliotecas utilizadas
from PIL import ImageGrab

import cv2
import numpy as np

tela_cascade = cv2.CascadeClassifier('tela.xml')

while(True):

    imagemcaptura = ImageGrab.grab(bbox=(300, 100, 800, 800)) #Dimensão da tela a ser capturada / bbox = boungind box onde os () definem as margens da captura

    frame = np.array(imagemcaptura) #Primeira coisa é converter para uma array de numpy

    frame =  cv2.cvtColor(imagemcaptura, cv2.COLOR_BGR2RGB) #Convertendo a imagem de BGR -> RGB

    pEb = cv2.cvtColor(imagemcaptura, cv2.COLOR_BGR2GRAY) #Convertendo a imagem de BGR -> GRAY

    faces = tela_cascade.detectMultiScale(pEb, 1.3, 5) #Detectando as faces
    for (x, y, w, h) in faces: #Desenhando as faces
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255, 0, 0),2)

    cv2.imshow('frame', frame) #Imprimindo o frame capturado acima

    if cv2.waitKey(1) == 27: #Flag pra a quebra do laço de repetição
        break

cv2.destroyAllWindows()









