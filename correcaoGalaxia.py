import cv2 as cv

src = cv.imread("imagens/galaxy_black.tiff", cv.IMREAD_GRAYSCALE)

img = cv.normalize(src,None, 0, 255,cv.NORM_MINMAX,dtype = cv.CV_8UC4)
contraste = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cont = contraste.apply(img)

cv.waitKey(0)
cv.destroyAllWindows()

# erro: é pequena demais e em bits