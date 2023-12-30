import cv2

# Задание: повернуть изображение на 45 градусов

img = cv2.imread('../cat.jpg')

height, weight = img.shape[:2]
center = (int(weight / 2), int(height / 2))
rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.7)
rotated = cv2.warpAffine(img, rotation_matrix, (weight, height))

cv2.imwrite('result.jpg', rotated)

cv2.imshow('source', img)
cv2.imshow('result', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
