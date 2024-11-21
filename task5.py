import os
os.system('cls')
print("\n")

print("Palindromi:")

for num in range(10, 1001):
    str_num = str(num)
    if str_num == str_num[::-1]:
        print(num)
