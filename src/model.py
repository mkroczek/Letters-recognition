from src.data_set import DataManager
import tensorflow as tf
import numpy as np
import cv2
from src.image_utils import prepare_image
import matplotlib.pyplot as plt

class Model():
    def __init__(self):
        self.categories = ["I", "O", "U", "W", "X"]
        self.data_manager = DataManager("Letters", self.categories, 50)
        self.model = None
        self.model_name = "letters.model"

    def train(self):
        '''
        Zakomentowane linijki sa do modelu rozpoznawania liter, aktualnie dziala na rozpoznawanie cyfr
        '''
        if not self.model:
            x,y = self.data_manager.create_training_set()
            x = tf.keras.utils.normalize(x, axis = 1)

            #mnist = tf.keras.datasets.mnist
            #(x_train, y_train), (x_test, y_test) = mnist.load_data()
            #x_train = tf.keras.utils.normalize(x_train, axis = 1)
            #x_test = tf.keras.utils.normalize(x_test, axis = 1)

            model = tf.keras.models.Sequential()
            model.add(tf.keras.layers.Flatten(input_shape = x.shape[1:]))
            # model.add(tf.keras.layers.Flatten())
            model.add(tf.keras.layers.Dense(units = 120, activation=tf.nn.relu))
            # model.add(tf.keras.layers.Dense(units = 10, activation=tf.nn.relu))
            model.add(tf.keras.layers.Dense(units = len(self.categories), activation=tf.nn.softmax))
            # model.add(tf.keras.layers.Dense(units = 10, activation=tf.nn.softmax))

            model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])
            model.fit(x, y, epochs = 20)
            # model.fit(x_train, y_train, epochs = 3)

            model.save(self.model_name)
            self.model = model

    def recognize(self, img):
        if self.model == None:
            return -1

        # img = img / 255.0
        for i in range(len(img)):
            print(img[i])
        img = np.array(img).reshape(-1 ,50, 50, 1)  # -> Wersja co rozpoznawania liter

        # image = cv2.imread("data/O.png")
        # image = prepare_image(image, 50, 50)

        # res = self.model.predict(image)
        # res = np.argmax(res)
        # print (self.categories[res])

        result = self.model.predict(img)
        result = np.argmax(result)
        return self.categories[result]
