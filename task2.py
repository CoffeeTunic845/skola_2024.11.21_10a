import os
os.system('cls')
print("\n")


n = int(input("Ievadiet skaitli n: "))

i = 1
while i <= n:
    row = "".join(str(j) for j in range(1, i + 1))
    print(row.rjust(n))
    i += 1
