import math

a = -0.9
b = 0.9
step = 0.05

num_steps = int(round((b - a) / step)) + 1


print(f"{'x':>8} | {'y':>12}")
print("-" * 23)

for i in range(num_steps):

    x = a + i * step
    

    if -1 <= x <= 1:
        # arccos^2(x) + arcsin^2(x)
        acos_val = math.acos(x)
        asin_val = math.asin(x)
        numerator = acos_val**2 + asin_val**2
        
        # sin^2(1 + x^2) - cos^2(1 - x^2)
        sin_arg = 1 + x**2
        cos_arg = 1 - x**2
        denominator = math.sin(sin_arg)**2 - math.cos(cos_arg)**2

        if abs(denominator) > 1e-12:
            y = numerator / denominator
            print(f"{x:8.2f} | {y:12.5f}")
        else:
            print(f"{x:8.2f} | {'деление на 0':>12}")
    else:
        print(f"{x:8.2f} | {'x вне [-1,1]':>12}")
