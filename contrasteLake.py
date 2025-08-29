import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


src = cv.imread("imagens/lake.png", cv.IMREAD_GRAYSCALE)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

equalizada = clahe.apply(src)
histograma = cv.calcHist([src], [0], None, [256], [0, 256])

plt.plot(histograma, color='black')
plt.title("Histograma da Imagem em Escala de Cinza")
plt.xlabel("Intensidade de Pixels")
plt.ylabel("Frequência da Intensidade")
plt.bar(range(256), histograma.ravel(), color='black', width=1)
plt.xlim([0, 256])
plt.show()


cv.imshow("original", src)
cv.imshow("histogramaEq", equalizada)
cv.waitKey(0)
cv.destroyAllWindows()

# qual efeito do histograma na imagem?
# Na imagem o histograma fez com que seus detalhes ficassem mais nítidos, como 
# se antes quem estivesse vendo tenha miopia e depois colocou os óculos
# o histograma diz que há vários pixels