# by rakuzan2weak
import random

print("Добро пожаловать в игру 'Dice Roll by rakuzan2weak'!")
print("В этой игре вы будете бросать кости и получать очки.")
print("У вас есть три попытки, чтобы набрать как можно больше очков.")
print("Удачи!")

score = 0
attempts = 3

while attempts > 0:
    input("Нажмите Enter, чтобы бросить кости...")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print("Вы бросили кости: {} и {}. Всего очков: {}".format(dice1, dice2, total))
    score += total
    attempts -= 1
    print("У вас {} попыток и {} очков.".format(attempts, score))

print("Игра окончена. Вы набрали {} очков.".format(score))