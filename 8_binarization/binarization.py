import cv2

# Задание: сделать бинаризацию изображения

img = cv2.imread('../cat.jpg')
_, threshold = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, 0)

cv2.imwrite('result.jpg', threshold)

cv2.imshow('source', img)
cv2.imshow('result', threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
