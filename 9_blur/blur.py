import cv2

# Задание: сделать размытие изображения

img = cv2.imread('../cat.jpg')
blured = cv2.blur(img, (7, 7))

cv2.imwrite('result.jpg', blured)

cv2.imshow('source', img)
cv2.imshow('result', blured)
cv2.waitKey(0)
cv2.destroyAllWindows()
