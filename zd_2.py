import math

product = 1

for n in range(1, 21):

    product *= (n**2 + math.sin(n**3)**3 + 1) / (n**2 + math.cos(n**2)**2 + math.sin(n))

print(product)