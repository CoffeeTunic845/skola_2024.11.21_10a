import os
os.system('cls')
print("\n")

n = int(input("Ievadiet skaitli n: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    print()
    i += 1

