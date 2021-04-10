# -*- coding: utf-8 -*-


### Importing the libraries ###
!pip3 install ktrain

import os.path
import numpy as np
import tensorflow as tf
import ktrain
from ktrain import text


### Loading the vaccine datasets

"""
dataset = tf.keras.utils.get_file(fname="!!!data folder name!!!",
                                  origin="!!!for each country like ../data/UK_vaccinaion_tweets.csv!!!",
                                  extract=True)
VAXX_DATADIR = os.path.join(os.path.dirname(dataset), 'vaccination_datasets')

print(os.path.dirname(dataset))
print(VAXX_DATADIR)
"""

data_train = pd.read_excel('EN_tweets.csv', dtype = str)

data_test = pd.read_excel('UK_vaccination_tweets.csv', dtype = str)

print("Size of train dataset: ",data_train.shape)
print("Size of test dataset: ",data_test.shape)

data_train.tail()
data_test.head()
### Creating the training and test sets

(x_train, y_train), (x_test, y_test), preproc = text.texts_from_folder(datadir=VAXX_DATADIR,
                                                                       classes=['pos','notr','neg'],
                                                                       maxlen=500,
                                                                       train_test_names=['train','test'],
                                                                       preprocess_mode='bert')

"""
(X_train, y_train), (X_test, y_test), preproc = text.texts_from_df(train_df=data_train,
                                                                   text_column = 'Tweets',
                                                                   label_columns = 'Sentiment',
                                                                   val_df = data_test,
                                                                   maxlen = 500,
                                                                   preprocess_mode = 'bert')
"""

### Building the BERT model ###

model = text.text_classifier(name='bert',
                             train_data=(x_train, y_train),
                             preproc=preproc)

### Training the BERT model ###

learner = ktrain.get_learner(model=model,
                             train_data=(x_train, y_train),
                             val_data=(x_test, y_test),
                             batch_size=6)

learner.fit_onecycle(lr=2e-5,
                     epochs=8)