from classes.BColors import BColors
from util.interactions import user_test_model
from classes.FatModel import FatModel
from classes.BColors import BColors
from classes.Displayer import Displayer

model = FatModel(epochs=1000)

try:
  Displayer.info_message("Construction du modèle...")
  Displayer.success_message("Modèle construit avec succès.")

  Displayer.info_message("Entraînement du modèle...")
  history = model.train()
  eval_result = model.evaluate()
  Displayer.success_message("Modèle entraîné avec succès.")
  
except Exception as e:
  Displayer.error_message(str(e))
  exit()

train_loss = history.history['loss'][-1]
val_loss = history.history['val_loss'][-1]

train_loss_color = BColors.getColorFromVal(train_loss, 0, 1)
val_loss_color = BColors.getColorFromVal(val_loss, 0, 1)


print("Train loss: " + train_loss_color + str(train_loss) + BColors.ENDC)
print("Validation loss: " + val_loss_color + str(val_loss) + BColors.ENDC)

# Let the user test
while True:
  user_test_model(model)