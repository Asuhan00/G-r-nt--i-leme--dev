import cv2
import numpy as np

img = cv2.imread("./Images/img_2.jpg")
print(img.shape)

x = 20
y = 10
#1 kanal mavi 2 kanal yeşil 3 kanal kırmızı
kanal = 0
#x,y kordinatındaki kanal kanalıkdaki deger
yogunluk = img[x,y,kanal]
print(yogunluk)

max_yogunluk = np.max(img)
min_yogunluk = np.min(img)
print(max_yogunluk)
print(min_yogunluk)

crap = img[100:500,100:500,0]
cv2.imshow("crap",crap)
cv2.imshow("img",img)





cv2.waitKey(0)
cv2.destroyAllWindows()



