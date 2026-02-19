# import numpy as np
# import cv2

# img=cv2.imread ('H:\1=jobayer\1=University\python\numpy\image/1.jpg')
# print(img)

# img_tined= img * np.array([0., 0., 1.])
# cv2.imsave('image/tinedd.jpg', img_tined)


import cv2
import numpy as np

img = cv2.imread(r"H:\1=jobayer\1=University\python\numpy\image\1.jpg")

if img is None:
    print("Error: Image not found. Check the path!")
    exit()

img_tined = img * np.array([.23, 0., 0.])

cv2.imwrite(r"H:\1=jobayer\1=University\python\numpy\image\tinted3.jpg", img_tined)


print(img_tined)