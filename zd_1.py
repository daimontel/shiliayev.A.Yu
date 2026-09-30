import math

total = 0

for n in range(1, 51):

    term = (1.9**(2*n + 1)) / (n**n + 2) * math.sin(n)

    total += term

print(total)


