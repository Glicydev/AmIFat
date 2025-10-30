from classes.BColors import BColors
from util.interactions import user_test_model
from classes.FatModel import FatModel
from classes.BColors import BColors

model = FatModel(epochs=1000)
model.build_model()

history = model.train()
eval_result = model.evaluate()
model.save("models/fatModel.keras")

train_loss = history.history['loss'][-1]
val_loss = history.history['val_loss'][-1]

train_loss_color = BColors.getColorFromVal(train_loss, 0, 1)
val_loss_color = BColors.getColorFromVal(val_loss, 0, 1)


print("Train loss: " + train_loss_color + str(train_loss) + BColors.ENDC)
print("Validation loss: " + val_loss_color + str(val_loss) + BColors.ENDC)

# Let the user test
while True:
  user_test_model(model)