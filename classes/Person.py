import numpy as np

class Person:
  def __init__(self, size, weight):
    self.__size = size
    self.__weight = weight
    self.__is_obese = self.__weight / pow(self.__size, 2) >= 25
    
  @property
  def is_obese(self):
    return self.__is_obese
  
  def to_array(self):
    return np.array([
      self.__size,
      self.__weight
    ])