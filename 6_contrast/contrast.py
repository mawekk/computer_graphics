import cv2


# Задание: изменить контраст изображения

def increase_contrast(image, lim):
    labImage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(labImage)

    clahe = cv2.createCLAHE(clipLimit=lim, tileGridSize=(8, 8))
    l_img = cv2.merge((clahe.apply(l), a, b))

    return cv2.cvtColor(l_img, cv2.COLOR_LAB2BGR)


img = cv2.imread('../cat.jpg')
result = increase_contrast(img, 5)

cv2.imwrite('result.jpg', result)

cv2.imshow('source', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
