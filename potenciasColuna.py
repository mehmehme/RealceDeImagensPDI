import cv2 as cv
import matplotlib.pyplot as plt

src = cv.imread("imagens/ressonancia.png", cv.IMREAD_GRAYSCALE)
contraste = cv.createCLAHE(clipLimit=5.0, tileGridSize=(4, 4))
cont = contraste.apply(src)

cv.imshow("original", src)
cv.imshow("contraste", cont)
cv.waitKey(0)
cv.destroyAllWindows()

# A imagem acabou ficando com bastante ruídos, mas agora conseguimos ver melhor a parte escura