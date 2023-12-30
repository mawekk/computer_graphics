import cv2


# Задание: сделать гистограмную эквайлизацию

img = cv2.imread('../cat.jpg')
equalized = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

cv2.imwrite('result.jpg', equalized)

cv2.imshow('source', img)
cv2.imshow('result', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
