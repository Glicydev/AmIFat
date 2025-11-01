from classes.BColors import BColors
from util.interactions import user_test_model
from classes.FatModel import FatModel
from classes.BColors import BColors
from classes.Displayer import Displayer

model = FatModel(epochs=1000)

try:
  Displayer.info_message("Construction du modèle...")
  model.build()
  Displayer.success_message("Modèle construit avec succès.")

  Displayer.info_message("Entraînement du modèle...")
  history = model.train()
  eval_result = model.evaluate()
  Displayer.success_message("Modèle entraîné avec succès.")

  model.save()
  
except Exception as e:
  Displayer.error_message(str(e))
  exit()

train_loss = history.history['loss'][-1]
val_loss = history.history['val_loss'][-1]

if (train_loss < val_loss):
  Displayer.warning_message("Attention : Le modèle semble surappris (overfitting).")

if (train_loss > 0.3):
  Displayer.warning_message("Attention : Le modèle n'a pas bien appris les données d'entraînement.")

if (val_loss > 0.3):
  Displayer.warning_message("Attention : Le modèle n'a pas bien généralisé sur les données de validation.")

train_loss_color = BColors.getColorFromVal(train_loss, 0, 1)
val_loss_color = BColors.getColorFromVal(val_loss, 0, 1)


print("Train loss: " + train_loss_color + str(train_loss) + BColors.ENDC)
print("Validation loss: " + val_loss_color + str(val_loss) + BColors.ENDC)

# Let the user test
while True:
  user_test_model(model)