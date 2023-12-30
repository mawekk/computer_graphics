import cv2

# Задание: найти canny edges на изображении

img = cv2.imread('../cat.jpg')
edges = cv2.Canny(img, 100, 250)
cv2.imwrite('result.jpg', edges)

cv2.imshow('source', img)
cv2.imshow('result', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
