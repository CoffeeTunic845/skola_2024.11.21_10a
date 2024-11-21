import os
os.system('cls')
print("\n")

countdown = 15
fib1, fib2 = 0, 1
print(fib1)

while countdown > 1:
    print(fib2)
    fib1, fib2 = fib2, fib1 + fib2
    countdown -= 1
    