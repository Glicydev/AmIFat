from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from classes.Person import Person, persons
from classes.BColors import BColors
import numpy as np

x = np.array([p.to_array() for p in persons])
y = np.array([1 if p.is_obese else 0 for p in persons])

x_train, x_test, y_train, y_test = train_test_split(
  x, y, test_size=1/3, train_size=2/3
)

epochs = 1000

model = Sequential([
  Dense(units=32, input_shape=([2])),
  Dense(units=1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam')
history = model.fit(x=x_train, y=y_train, epochs=epochs)

test_loss = model.evaluate(x_test, y_test)
test_loss_color = BColors.getColorFromVal(test_loss, 0, 1)

print("Test loss: " + test_loss_color + str(test_loss) + BColors.ENDC)

while True:
  size = float(input('Taille (M): '))
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
  
  if input("Quitter ? (o/n)").lower() == "o": 
    break