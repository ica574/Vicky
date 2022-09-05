# Name: trainer.py
# Author: Isaac Cilia Attard
# Date: 26/08/2022
# Description: Trains the deep learning model on the commands file in order for the neural network to perform text classification.

import yaml
import json
import numpy as np
import tensorflow as tf
import os

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

data = yaml.safe_load(open('nlu\\Commands.yml').read())

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(str(command['input'].lower()))
    outputs.append('{}\{}'.format(command['entity'], command['action']))

# Create a dataset
# Choose a level of tokenisation: words, chars, BPEs

# Create input data
max_sent = max([len(x) for x in inputs])

# Create arrays
input_data = np.zeros((len(inputs), max_sent, 256), dtype='float32')

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i, k, int(ch)] = 1.0

# output_data = to_categorical(output_data, len(output_data))
print(input_data[0].shape)

labels = set(outputs)

fwrite = open('nlu\entities.txt', 'w', encoding='utf-8')
for label in labels:
    fwrite.write(label + '\n')
fwrite.close()

labels = open('nlu\entities.txt', 'r', encoding='utf-8').read().split('\n')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

output_data = []

for output in outputs:
    output_data.append(label2idx[output])

output_data = to_categorical(output_data, len(labels))

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(labels), activation="softmax"))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.fit(input_data, output_data, epochs=256)

model.save('nlu\classificationModel.h5')