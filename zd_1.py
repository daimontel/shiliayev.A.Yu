def product_in_range(arr, x, y):
    # Убедимся, что x <= y (если пользователь перепутал порядок)
    left, right = min(x, y), max(x, y)

    product = 1.0
    found = False

    for value in arr:
        if left <= value <= right:
            product *= value
            found = True

    if not found:
        print("Нет элементов в отрезке [{}, {}].".format(left, right))
        return 1.0

    return product



if __name__ == "__main__":
    # Ввод массива как строки чисел через пробел
    arr_input = input("Введите элементы массива (через пробел): ")
    arr = [float(x) for x in arr_input.split()]

    x = float(input("Введите X: "))
    y = float(input("Введите Y: "))

    result = product_in_range(arr, x, y)
    print("Произведение элементов в отрезке:", result)
