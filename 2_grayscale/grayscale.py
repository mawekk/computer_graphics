import cv2

# Задание: перевести изображение в grayscale

img = cv2.imread('../cat.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('result.jpg', gray)

cv2.imshow('source', img)
cv2.imshow('result', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
