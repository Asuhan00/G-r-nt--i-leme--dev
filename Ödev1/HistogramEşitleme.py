import cv2
import matplotlib.pyplot as plt
import numpy as np


def fotografin_histogramini_olustur(foto, L):
    histogram, bins = np.histogram(foto, bins=L, range=(0, L))
    return histogram


def p_Hesapla(foto, L):
    histogram = fotografin_histogramini_olustur(foto, L)
    return histogram / foto.size 


def t_Hesapla(p):
    return np.cumsum(p)


def histogram_esitleme(foto, L):
    p = p_Hesapla(foto, L)
    t = t_Hesapla(p)
    eksi_t = (L-1) * t
    shape = foto.shape
    ravel = foto.ravel() #tek boyuta donuştür
    hist_es_foto = np.zeros_like(ravel)
    for i, pixel in enumerate(ravel):
        hist_es_foto[i] = eksi_t[pixel]
    return hist_es_foto.reshape(shape).astype(np.uint8)
    

if __name__ == "__main__":
    L = 256
    foto = cv2.imread("./Images/img_6.jpg", 0)
    hist_es_foto = histogram_esitleme(foto, L)
    yanyana = np.hstack((foto, hist_es_foto))
    plt.imshow(yanyana, cmap="gray")
    plt.show()