import cv2


fn='/home/tony/图片/123.png'
image=cv2.imread(fn)
cv2.imshow('Hello World!',image)
cv2.waitKey(0)