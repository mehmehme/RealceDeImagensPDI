import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


src = cv.imread("imagens/mesa.png", cv.IMREAD_GRAYSCALE)
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

equalizada = clahe.apply(src)
histograma = cv.calcHist([src], [0], None, [256], [0, 256])
histogramaEq = cv.calcHist([equalizada], [0], None, [256], [0, 256])

# histograma
plt.plot(histograma, color='black')
plt.title("Histograma da Imagem em Escala de Cinza")
plt.xlabel("Intensidade de Pixels")
plt.ylabel("Frequência da Intensidade")
plt.bar(range(256), histograma.ravel(), color='black', width=1)
plt.xlim([0, 256])
plt.show()

# # histograma equalizado
# plt.plot(histogramaEq, color='black')
# plt.title("Histograma Equalizado")
# plt.xlabel("Intensidade de Pixels")
# plt.ylabel("Frequência da Intensidade")
# plt.bar(range(256), histogramaEq.ravel(), color='black', width=1)
# plt.xlim([0, 256])
# plt.show()


cv.imshow("original", src)
cv.imshow("histogramaEq", equalizada)
cv.waitKey(0)
cv.destroyAllWindows()