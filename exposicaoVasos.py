import cv2 as cv
from matplotlib import pyplot as plt

norm = cv.imread("imagens/vaso normal.png")
super = cv.imread("imagens/vaso super.png")
sub = cv.imread("imagens/vaso sub.png")

hiNo = cv.calcHist([norm], [0], None, [256], [0, 256])
hiSup = cv.calcHist([super], [0], None, [256], [0, 256])
hiSub = cv.calcHist([sub], [0], None, [256], [0, 256])

plt.hist(hiNo, bins=30, alpha=0.5, label='Normal', color='blue')
plt.hist(hiSup, bins=30, alpha=0.5, label='Super', color='red')
plt.hist(hiSub, bins=30, alpha=0.5, label='Sub', color='yellow')

plt.title('Histogramas Sobrepostos')
plt.legend('123')
plt.show()


cv.waitKey(0)
cv.destroyAllWindows()