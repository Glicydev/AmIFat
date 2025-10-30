from keras import *
from keras.models import Sequential
from keras.layers import Dense
from classes.Person import Person, persons
from classes.BColors import BColors
import numpy as np

x = np.array([p.to_array() for p in persons])
y = np.array([1 if p.is_obese else 0 for p in persons])
epochs = 1000

model = Sequential([
  Dense(units=32, input_shape=([2])),
  Dense(units=1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x=x, y=y, epochs=epochs)


size = float(input('Taille (mètres): '))
weight = int(input('poids (Kg): '))

user_person = Person(size, weight)
user_person_array = np.array([user_person.to_array()])

prediction = model.predict(user_person_array)[0][0]

obese_chances = round(prediction * 100, 2)
not_obese_chances = 100 - obese_chances

percentage_Color = BColors.getColorFromVal(obese_chances, 0, 100)

print("\n")
print(BColors.OKBLUE + "==================================" + BColors.ENDC)
print("Prédiction du modèle: " + percentage_Color + str(round(prediction, 3)) + BColors.ENDC)
print(BColors.OKBLUE + "============ Résultat ============" + BColors.ENDC)
print("Chances d'être obèse:  " + percentage_Color + str(obese_chances) + "%" + BColors.ENDC)
print("Chances de ne pas être obèse:  " + percentage_Color + str(not_obese_chances) + "%" + BColors.ENDC)
print(BColors.OKBLUE + "==================================" + BColors.ENDC)