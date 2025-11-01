from util.dataset import getDataset
from keras.models import Sequential, load_model
from keras.layers import Dense
from classes.Person import Person
import numpy as np


class FatModel:
  def __init__(self, epochs=1000, path='models/fatModel.keras'):
    self.__epochs = epochs
    self.__path = path
  
    
  def __load_dataset(self):
    self.__x_train, self.__x_test, self.__y_train, self.__y_test = getDataset()

  def __check_had_model(self):
    if not hasattr(self, '_FatModel__model'):
      raise Exception("Le modèle n'a pas été construit ou chargé. Veuillez d'abord appeler build_model() ou load_model().")

  def build(self):
    self.__load_dataset()

    # Build the model
    self.__model = Sequential([
      Dense(units=32, input_shape=([2])),
      Dense(units=1, activation='sigmoid')
    ])

  def load_from_source(self):
    self.__model = load_model(self.__path)
    
  def train(self):
    self.__check_had_model()

    # Compile, fit and display metrics
    self.__model.compile(loss='binary_crossentropy', optimizer='adam')
    history = self.__model.fit(
      x=self.__x_train,
      y=self.__y_train,
      epochs=self.__epochs,
      validation_split=0.2
    )

    return history
      
  def evaluate(self):
    self.__check_had_model()

    return self.__model.evaluate(self.__x_test, self.__y_test)
  
  def predict(self, size, weight):
    self.__check_had_model()

    person = Person(size=size, weight=weight)
    input_data = np.array([person.to_array()])
    return self.__model.predict(input_data)
  
  def save(self):
    self.__model.save(self.__path)