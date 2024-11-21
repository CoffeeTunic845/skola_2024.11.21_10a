import os
os.system('cls')
print("\n")

countdown = 15
fib0 = 0
fib1 = 0
fib2 = 1
print(fib1)
print(fib2)

while countdown > 0:
    fib0 = fib1 + fib2
    print(fib0)
    fib1 = fib2
    fib2 = fib0
    countdown -= 1
    