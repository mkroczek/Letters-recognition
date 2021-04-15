import cv2
import  numpy as np
import matplotlib.pyplot as plt


def prepare_image(img, img_width, img_height):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_AREA)
    newimg = [[0.0]*len(img) for i in range(len(img[0]))]
    for i in range(len(img)):
        for j in range(len(img[i])):
            # img[i][j] = 1 - img[i][j]/255.0
            newimg[i][j] = 1 - img[i][j]/255.0
    # newimg = np.array(img).reshape(-1, img_width, img_height, 1)
    # plt.imshow(newimg)
    # plt.show()
    return newimg

