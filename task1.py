import os
os.system('cls')
print("\n")

print("Perfektie skaitļi diapazonā no 1 līdz 10,000:")

for num in range(1, 10001):
    divisor_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisor_sum += i
    if divisor_sum == num:
        print(num)

