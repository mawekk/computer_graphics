import cv2

# Задание: отразить изображение по нижней границе

img = cv2.imread('../cat.jpg')
flipped = cv2.flip(img, 0)
cv2.imwrite('result.jpg', flipped)

cv2.imshow('source', img)
cv2.imshow('result', flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
