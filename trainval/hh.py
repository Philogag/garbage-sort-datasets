import cv2


with open('./dataset/train_data.txt', 'r') as f:
    datas = f.read().split('\n')

path, bbox = datas[0].split()
print(path)
img = cv2.imread("../trainval" + path)
cv2.imshow("hh", img)
cv2.waitKey()
