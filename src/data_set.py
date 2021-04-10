import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
import src.image_utils as img_utils

class DataManager():
    def __init__(self, data, categories, img_size):
        self.DATA = data
        self.CATEGORIES = categories
        self.IMG_SIZE = img_size

    def create_training_data(self):
        training_data = []
        for category in self.CATEGORIES:
            path = os.path.join(self.DATA, category)
            class_num = self.CATEGORIES.index(category)
            for image in os.listdir(path):  # iterating through all images
                # image_array = cv2.imread(os.path.join(path, image), cv2.IMREAD_GRAYSCALE)  # reading image in grayscale
                image_array = cv2.imread(os.path.join(path, image))  # reading image in grayscale
                # new_array = cv2.resize(image_array, (self.IMG_SIZE, self.IMG_SIZE))
                new_array = img_utils.prepare_image(image_array, self.IMG_SIZE, self.IMG_SIZE)
                training_data.append([new_array, class_num])
                # if (category == self.CATEGORIES[0]):
                #     for i in range(len(new_array)):
                #         print(new_array[i])
                # if (category == self.CATEGORIES[0]):
                #     plt.imshow(np.array(new_array), cmap="gray")
                #     plt.show()
        return training_data


    def create_training_set(self):
        training_data = self.create_training_data()
        random.shuffle(training_data)
        x = []
        y = []
        for feature, label in training_data:
            x.append(feature)
            y.append(label)

        # convert lists to np.array
        x = np.array(x).reshape(-1, self.IMG_SIZE, self.IMG_SIZE, 1)
        y = np.array(y)
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

