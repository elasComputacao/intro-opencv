# Importando as bibliotecas Opencv(cv2) e numpy(nomeada como np)
import cv2
import numpy as np

# Antes de editar faça uma cópia(fork) desse repositório em sua conta
# Todas os exemplos das representações dos 7 tipos de frisos vistos aqui estão presentes no pacote "exemploFrisos"

'''
Uso da Opencv no projeto:
imread
imwrite
flip (0: reflete horizontalmente | 1: reflete verticalmente | -1: reflete horizontalmente e verticalmente)

Uso da Numpy no projeto:
hstack
vstack
'''


#Lendo uma imagem(presente no pacote "imagensEntrada" e armazenando na variável img
#Para que os frisos fiquem visivelmente melhores, é esperado que a imagem seja assimentrica tanto em relação ao eixo x quanto em relação ao eixo x 

img = cv2.imread('imagensEntrada/forma.png')

#1: Translação (sucessivas repetições de um motivo)


#2: Reflexão Horizontal + Translação (sucessivas repetições de um motivo + reflexão em relação ao eixo X)


#3: Reflexão Vertical + Translação (Reflexão de um motivo em relação ao eixo Y, com sucessivas repetições)


'''
Escrevendo uma nova imagem, tendo como base as dimensões da imagem de entrada
Atribuímos a ela a cor branco, em RGB (255,255,255)
'''

img2 = cv2.imread('imagensEntrada/forma.png')
for y in range(0, img2.shape[0]):
	for x in range(0, img.shape[1]):
		img2[x,y] = (255, 255, 255)


#4: Reflexão Horizontal + Deslizante (reflexão em relação ao eixo X com deslizes)

#5: Rotação 180 (rotação de 180 graus de um motivo com sucessivas repetições)

#6: Reflexão Horizontal + Vertical (Reflexão simultânea de um motivo em relação aos eixos X e Y)


#7:  Reflexão Horizontal + Vertical + Deslizante (Acrescenta deslizes ao tipo de friso anterior)
