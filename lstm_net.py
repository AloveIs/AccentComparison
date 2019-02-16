# LSTM for sequence classification in the IMDB dataset

import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence

# fix random seed for reproducibility
numpy.random.seed(7)

# load the dataset
# it sould be a vector of lists, where each list represent the time-series
(X_train, y_train) = np.array([[0]*10]*100)
(X_test, y_test) = np.array([[0]*10]*100)

# truncate and pad the sequences to have them all of the same lenght
# required by keras
max_length = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

# create the model
embedding_vecor_length = 32
model = Sequential()
# possible embedding layer
#model.add(Embedding(input_dim, output_dim, input_length=...))
model.add(LSTM(100, input_dim=input_size))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())
model.fit(X_train, y_train, epochs=3, batch_size=64)

# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=1)
print("Accuracy: %.2f%%" % (scores[1]*100))
