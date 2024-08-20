
from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
# dice_num = 6 would error out, "reproducing the bug"
print(dice_images[dice_num])
