import cv2


# Задание: изменить яркость изображения

def increase_brightness(image, value):
    h, s, v = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    return cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)


img = cv2.imread('../cat.jpg')
result = increase_brightness(img, 50)

cv2.imwrite('result.jpg', result)

cv2.imshow('source', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
