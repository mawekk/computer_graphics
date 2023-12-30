# Основы компьютерной графики и обработки изображений. Отчет о выполненных заданиях

## Исходное изображение

<img src="cat.jpg" alt="alt text" width="500">

## Задания

### 1. Найти canny edges на изображении
```python
img = cv2.imread('../cat.jpg')
edges = cv2.Canny(img, 100, 250)
```
Результат:

<img src="1_canny_edges/result.jpg" alt="alt text" width="500">

### 2. Перевести изображение в grayscale
```python
img = cv2.imread('../cat.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
Результат:

<img src="2_grayscale/result.jpg" alt="alt text" width="500">

### 3. Отразить изображение по нижней границе
```python
img = cv2.imread('../cat.jpg')
flipped = cv2.flip(img, 0)
```
Результат:

<img src="3_flip_bottom/result.jpg" alt="alt text" width="500">

### 4. Повернуть изображение на 45 градусов
```python
img = cv2.imread('../cat.jpg')

height, weight = img.shape[:2]
center = (int(weight / 2), int(height / 2))
rotation_matrix = cv2.getRotationMatrix2D(center, -45, 0.7)
rotated = cv2.warpAffine(img, rotation_matrix, (weight, height))
```
Результат:

<img src="4_rotate_45/result.jpg" alt="alt text" width="500">

### 5. Изменить яркость изображения
```python
def increase_brightness(image, value):
    h, s, v = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    return cv2.cvtColor(cv2.merge((h, s, v)), cv2.COLOR_HSV2BGR)


img = cv2.imread('../cat.jpg')
result = increase_brightness(img, 50)
```
Результат:

<img src="5_brightness/result.jpg" alt="alt text" width="500">

### 6. Изменить контраст изображения
```python
def increase_contrast(image, lim):
    labImage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(labImage)

    clahe = cv2.createCLAHE(clipLimit=lim, tileGridSize=(8, 8))
    l_img = cv2.merge((clahe.apply(l), a, b))

    return cv2.cvtColor(l_img, cv2.COLOR_LAB2BGR)


img = cv2.imread('../cat.jpg')
result = increase_contrast(img, 5)
```
Результат:

<img src="6_contrast/result.jpg" alt="alt text" width="500">

### 7. Сделать гистограмную эквайлизацию
```python
img = cv2.imread('../cat.jpg')
equalized = cv2.equalizeHist(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
```
Результат:

<img src="7_histogram_equalization/result.jpg" alt="alt text" width="500">

### 8. Сделать бинаризацию изображения
```python
img = cv2.imread('../cat.jpg')
_, threshold = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, 0)
```
Результат:

<img src="8_binarization/result.jpg" alt="alt text" width="500">

### 9. Сделать размытие изображения
```python
img = cv2.imread('../cat.jpg')
blured = cv2.blur(img, (7, 7))
```
Результат:

<img src="9_blur/result.jpg" alt="alt text" width="500">

### 10. Применить операцию эрозии к изображению
```python
img = cv2.imread('../cat.jpg')
kernel = numpy.ones((5, 5), numpy.uint8)
result = cv2.erode(img, kernel)
```
Результат:

<img src="10_erosion/result.jpg" alt="alt text" width="500">
