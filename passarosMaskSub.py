import cv2 as cv

src = cv.imread("imagens/passaros.webp", cv.IMREAD_GRAYSCALE)
mask = cv.imread("imagens/mask.png", cv.IMREAD_GRAYSCALE)

subtracao = cv.subtract(src,mask)


cv.imshow("original", src)
cv.imshow("Subtraido", subtracao)

cv.waitKey(0)
cv.destroyAllWindows()

# tudo escuro