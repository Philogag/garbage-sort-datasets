import cv2


with open('../dataset/test_data.txt', 'r') as f:
    datas = f.read().split()
    image_path = datas[0].split()[0]

image_path = '.' + image_path
print(image_path)
img = cv2.imread(image_path)
print(img)
cv2.imshow("hh", img)
cv2.waitKey()

