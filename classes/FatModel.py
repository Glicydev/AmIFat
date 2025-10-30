from util.dataset import getDataset
from keras.models import Sequential
from keras.layers import Dense
from classes.Person import Person
import numpy as np


class FatModel:
  
  def __init__(self, epochs=1000):
    self.__epochs = epochs
    self.__init_with_dataset()
    
    
  def __init_with_dataset(self):
    self.__x_train, self.__y_train, self.__x_val, self.__y_val, self.__x_test, self.__y_test = getDataset()
    
  def build_model(self):
    # Build the model
    self.__model = Sequential([
      Dense(units=32, input_shape=([2])),
      Dense(units=1, activation='sigmoid')
    ])
    
  def train(self):
    # Compile, fit and display metrics
    self.__model.compile(loss='binary_crossentropy', optimizer='adam')
    return self.__model.fit(
      x=self.__x_train,
      y=self.__y_train,
      epochs=self.__epochs,
      validation_data=(self.__x_val, self.__y_val)
    )
    
  def evaluate(self):
    return self.__model.evaluate(self.__x_test, self.__y_test)
  
  def predict(self, size, weight):
    person = Person(size=size, weight=weight)
    input_data = np.array([person.to_array()])
    return self.__model.predict(input_data)
  
  def save(self, path):
    self.__model.save(path)