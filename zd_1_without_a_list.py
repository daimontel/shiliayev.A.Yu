import math

a = -5.0
b = 5.0
step = 0.5

x = a


print(f"{'x':>8} | {'y':>12}")
print("-" * 23)

while True:

    if x < 0:
        y = x**2 + 2*x
    else:
        y = math.sqrt(x) + 1
    
    print(f"{x:8.2f} | {y:12.5f}")

    x += step
    
    if x > b + 1e-9:
        break
