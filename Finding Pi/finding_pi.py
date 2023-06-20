import math

print(f"Pi------ {math.pi}")

sudoPi = 3
oddCount = False
numberOfIncrements = 50000

for i in range(4, numberOfIncrements, 2):
    if oddCount:
        sudoPi -= 4/((i-2)*(i-1)*i)
    else:
        sudoPi += 4/((i-2)*(i-1)*i)
    oddCount = not oddCount

print(f"Sudo-Pi- {sudoPi}")
print(f"increments {numberOfIncrements}")