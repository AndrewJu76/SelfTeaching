import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from collections import Counter

if __name__ == '__main__':
    data = []
    row,col = 0,0
    with Image.open(".\\images\\squirrel.jpg") as img:
        # print(img.size)
        m, n = img.size
        for i in range(m):
            for j in range(n):
                x, y, z = img.getpixel((i, j))
                data.append([x / 256.0, y / 256.0, z / 256.0])
    row = m
    col = n
    imgData = np.array(data)
    print(imgData.shape,row,col)
    label = KMeans(n_clusters=10).fit_predict(imgData)
    # res = Counter(label)
    # print(dict(res))
    label = label.reshape([row,col])
    # print(label.shape)
    pic_new = Image.new("L", (row, col))
    for i in range(row):
        for j in range(col):
            # print(label[i][j])
            pic_new.putpixel((i, j), int(256 / (label[i][j]+2)))
    pic_new.save(".\\saved_images\\squirrel by Kmeans.jpg")