import os
os.system('cls')
print("\n")

import random

counter = 0
rolls = 50

print("Skaitļi kas iskrita:")
while rolls > 0:
    number = random.randint(1, 6)
    if number == 6:
        counter += 1
    rolls -= 1
    print(number)

print("6 izkrita", counter, "reizes.")