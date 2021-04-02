import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle

DATA = "C:/Users/zgrod/Documents/Python/Letters-recognition/Letters"
CATEGORIES = ["I", "O", "U", "W", "X"]
IMG_SIZE = 50

training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA, category)
        class_num = CATEGORIES.index(category)
        for image in os.listdir(path):  # iterating through all images
            image_array = cv2.imread(os.path.join(path, image), cv2.IMREAD_GRAYSCALE)  # reading image in grayscale
            new_array = cv2.resize(image_array, (IMG_SIZE, IMG_SIZE))
            training_data.append([new_array, class_num])
            # plt.imshow(np.array(new_array), cmap="gray")
            # plt.show()


def create_training_set():
    create_training_data()
    random.shuffle(training_data)
    x = []
    y = []
    for feature, label in training_data:
        x.append(feature)
        y.append(label)

    # convert lists to np.array
    x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    return x,y


"""x, y = create_training_set()
pickle_out = open("x.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open("x.pickle", "rb")
X = pickle.load(pickle_in)

print(X[1])"""

