import numpy as np 
import cv2
img = cv2.imread('YOUR_IMAGE_PATH ',0)

template = cv2.imread('YOUR_TEMPLATE_PATH',0)

h,w = template.shape

methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,cv2.TM_CCORR,cv2.TM_CCORR_NORMED,cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val , max_val , min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF_NORMED,cv2.TM_SQDIFF]:
        location = min_loc
    else:
        location = max_loc
bottom_right = (location[0]+w,location[1]+h)
cv2.rectangle(img2,location,bottom_right,(255,255,255),5)
img = cv2.resize(img2,(400,400))
cv2.imshow('SHOW',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
