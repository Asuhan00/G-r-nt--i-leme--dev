import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./Images/img.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gaussian = cv2.GaussianBlur(gray,(3,3),0)

compass0 =np.array([[-1,-1,-1],[1,-2,1],[1,1,1]])
compass45 =np.array([[-1,-1,1],[-1,-2,1],[1,1,1]])
compass90 =np.array([[-1,1,1],[-1,-2,1],[-1,1,1]])
compass135 =np.array([[1,1,1],[-1,-2,1],[-1,-1,1]])
compass180 =np.array([[1,1,1],[1,-2,1],[-1,-1,-1]])
compass225 =np.array([[1,1,1],[1,-2,-1],[1,-1,-1]])
compass270 =np.array([[1,1,-1],[1,-2,-1],[1,1,-1]])
compass315 =np.array([[1,-1,-1],[1,-2,-1],[1,1,1]])

img_compass0 = cv2.filter2D(img_gaussian,-1,compass0)
img_compass45 = cv2.filter2D(img_gaussian,-1,compass45)
img_compass90 = cv2.filter2D(img_gaussian,-1,compass90)
img_compass135 = cv2.filter2D(img_gaussian,-1,compass135)
img_compass180 = cv2.filter2D(img_gaussian,-1,compass180)
img_compass225 = cv2.filter2D(img_gaussian,-1,compass225)
img_compass270 = cv2.filter2D(img_gaussian,-1,compass270)
img_compass315 = cv2.filter2D(img_gaussian,-1,compass315)

cv2.imshow("Original Image",img)
cv2.imshow("Compass0",img_compass0)
cv2.imshow("Compass45",img_compass45)
cv2.imshow("Compass90",img_compass90)
cv2.imshow("Compass135",img_compass135)
cv2.imshow("Compass180",img_compass180)
cv2.imshow("Compass225",img_compass225)
cv2.imshow("Compass270",img_compass270)
cv2.imshow("Compass315",img_compass315)



cv2.waitKey(0)
cv2.destroyAllWindows()