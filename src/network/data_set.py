import numpy as np
import os
import cv2
import random
import src.utils.image_utils as img_utils

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
                image_array = cv2.imread(os.path.join(path, image))  # reading image in grayscale
                new_array = img_utils.prepare_image(image_array, self.IMG_SIZE, self.IMG_SIZE)
                training_data.append([new_array, class_num])
        return training_data


    def create_training_set(self):
        training_data = self.create_training_data()
        random.shuffle(training_data)
        x = []
        y = []
        for feature, label in training_data:
            feature = np.array(feature)
            x.append(feature.flatten())
            y.append(label)
        return x,y

    def create_test_data(self, directory):
        x = []
        y = []
        for category in self.CATEGORIES:
            path = os.path.join(directory, category)
            class_num = self.CATEGORIES.index(category)
            for image in os.listdir(path):  # iterating through all images
                image_array = cv2.imread(os.path.join(path, image))  # reading image in grayscale
                new_array = img_utils.prepare_image(image_array, self.IMG_SIZE, self.IMG_SIZE)
                new_array = np.array(new_array)
                x.append(new_array.flatten())
                y.append(class_num)
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

