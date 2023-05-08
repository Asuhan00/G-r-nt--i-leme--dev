import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogramGerme(foto):
    yeni_max = 255
    yeni_min = 0
    old_max = np.max(foto)
    old_min = np.min(foto)
    s = (((yeni_max-yeni_min)/(old_max-old_min))*(foto-old_min)) + yeni_min
    return s

foto = cv2.imread("./Images/img_6.jpg",0)
yeni_foto = histogramGerme(foto)
plt.imshow(np.hstack((foto,yeni_foto)),cmap="gray")
plt.show()