import cv2
import numpy as np
import  numpy as ny
"""افضل نوع من انواع ال edges detection"""
img=cv2.imread("hand.jpg",0)
canny=cv2.Canny(img,100,200)
canny=np.uint8(np.absolute(canny))
cv2.imshow("canny",canny)
cv2.imshow("img",img)
cv2.imwrite("D:\projects\python_pycharm\Laplacian\output_of_canny.jpg",canny)
cv2.waitKey(0)
cv2.destroyWindow()