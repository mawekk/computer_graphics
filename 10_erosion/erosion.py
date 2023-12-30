import cv2
import numpy

# Задание: применить операцию эрозии к изображению

img = cv2.imread('../cat.jpg')
kernel = numpy.ones((5, 5), numpy.uint8)
result = cv2.erode(img, kernel)

cv2.imwrite('result.jpg', result)

cv2.imshow('source', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
