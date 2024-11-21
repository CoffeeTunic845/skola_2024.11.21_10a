import os
os.system('cls')
print("\n")

i = 6
while i > 0:
    print(i)
    i -= 1

while True:
    n = int(input("Cik reižu? "))
    if n < 0:
        continue
    else:
        break