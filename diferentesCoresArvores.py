import cv2 as cv
import numpy as np

src = cv.imread("imagens/tree.webp")
b, g, r = cv.split (src)

semAzul = r
negativa = 255 - np.array(src)


cv.imshow("original", src)
cv.imshow("invertido", negativa)
cv.imshow("invertido", semAzul)

cv.waitKey(0)
cv.destroyAllWindows()