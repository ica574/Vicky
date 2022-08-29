# Name: Classifier.py
# Author: Isaac Cilia Attard
# Date: 26/08/2022
# Description: Employs the trained deep learning model in order to classify commands given by the user.

from tensorflow.keras.models import load_model
import numpy as np

labels = open('NLP\entities.txt', 'r', encoding='utf-8').read().split('\n')
model = load_model('NLP\classificationModel.h5')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

def classify(text):
    x = np.zeros((1, 24, 256), dtype='float32')

    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0
    
    out = model.predict(x)
    idx = out.argmax()

    print('Text: "{}" is classified as "{}"'.format(text, idx2label[idx]))
    return idx2label[idx]