import math

def calculate_y(x):

    if x <= 0 or (2 - x) <= 0:
        return "Ошибка: значение x выходит за пределы области определения функции."
    x_to_x = x ** x                 # x^x
    x_to_inv_x = x ** (1 / x)       # x^(1/x)
    
    # e^(x^x) * ln(2 + x^(1/x))
    term1 = math.exp(x_to_x) * math.log(2 + x_to_inv_x)
    
    # 2^x * ln(2 - x)
    term2 = (2 ** x) * math.log(2 - x)
    
    # -e^(2 / x^x)
    term3 = -math.exp(2 / x_to_x)
    
    y = term1 + term2 + term3
    return y

x_value = int(input('ведите x = '))
result = calculate_y(x_value)

print(f"При x = {x_value} значение функции y = {result:.5f}")
print(f"Для сравнения: аналитическое решение e*ln(3) - e^2 ≈ {math.e * math.log(3) - math.e**2}")
