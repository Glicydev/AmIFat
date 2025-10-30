from classes.BColors import BColors
import numpy as np


def user_test_model(model):
  size = float(input('Taille (M): '))
  weight = int(input('poids (Kg): '))

  prediction = model.predict(size, weight)[0][0]

  obese_chances = round(prediction * 100, 2)
  not_obese_chances = 100 - obese_chances

  percentage_Color = BColors.getColorFromVal(obese_chances, 0, 100)

  print("\n")
  print(BColors.OKBLUE + "\n==================================" + BColors.ENDC)
  print("Prédiction du modèle: " + percentage_Color + str(round(prediction, 3)) + BColors.ENDC)
  print(BColors.OKBLUE + "============ Résultat ============" + BColors.ENDC)
  print("Chances d'être obèse:  " + percentage_Color + str(obese_chances) + "%" + BColors.ENDC)
  print("Chances de ne pas être obèse:  " + percentage_Color + str(not_obese_chances) + "%" + BColors.ENDC)
  print(BColors.OKBLUE + "==================================\n" + BColors.ENDC)
  
  if input("Quitter ? (o/n)").lower() == "o": 
    exit()