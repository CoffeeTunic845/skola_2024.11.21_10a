import os
os.system('cls')
print("\n")

import random

counter = 0
rolls = 50

while rolls > 0:
    dice = [1, 2, 3, 4, 5, 6]
    if random.choice(dice) == 6:
        counter += 1
    rolls -= 1

print("6 izkrita", counter, "reizes.")