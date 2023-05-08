import cv2
import numpy as np
import matplotlib.pyplot as plt


def foto_negatifi(foto):
    L = max_yogunluk = np.max(foto)
    #numpy burada sabit bir degerden matris çıkarmaya çalıştığında her bir matris degeri için hesaplar exp: neg_foto[0,0] = L - foto[0,0]
    negatif_foto = L - foto
    return negatif_foto

def log_donusumu(foto,c):
    foto = foto.astype(float)
    s= c* np.log(1+foto)
    return s.astype(np.uint8)

def foto_rescale(foto):
    s = foto.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)

foto = cv2.imread("./Images/img_2.jpg",0)


print(foto.shape)

#2 matrisi birleştiriyor. yanyana koyuyor.
yanyana = np.hstack((foto,foto_negatifi(foto),foto_rescale(log_donusumu(foto,c=1))))

plt.imshow(yanyana, cmap="gray")

plt.show()
