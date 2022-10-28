import os

import numpy as np
import tensorflow as tf
from django.conf import settings
from keras.models import load_model
from keras.preprocessing import image

model = load_model('patients/model_cnn.h5')


def prepare_image(file):
    img = image.load_img(file, target_size=(160, 160))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


def predict_image(file):
    try:
        img = prepare_image(file)
        predictions = model.predict(img)
        return np.argmax(predictions)
    except Exception as e:
        print(e)
        return "Error"
