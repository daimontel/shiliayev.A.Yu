
def task1_with_list():
    try:
        n = int(input("Введите количество чисел N: "))
        if n <= 0:
            print("N должно быть положительным.")
            return
    except ValueError:
        print("Ошибка ввода N.")
        return

    nums = []
    print(f"Введите {n} целых чисел (каждое с новой строки или через пробел):")
    # Читаем все числа, поддерживая ввод через пробел в одной строке
    while len(nums) < n:
        line = input()
        parts = list(map(int, line.split()))
        nums.extend(parts)

    max_len = 0
    best_sum = 0

    i = 0
    while i < n:
        # Начало нового возрастающего участка
        start = i
        current_len = 1
        current_sum = nums[i]

        # Растём, пока следующее число строго больше текущего
        while i + 1 < n and nums[i + 1] > nums[i]:
            i += 1
            current_len += 1
            current_sum += nums[i]

        # Обновляем лучший результат
        if current_len > max_len:
            max_len = current_len
            best_sum = current_sum

        i += 1  # Переход к следующему числу после участка

    if max_len == 0 and n > 0:
        # На случай, если все числа одинаковые или убывают — самый длинный участок длины 1
        max_len = 1
        best_sum = nums[0]

    print(f"Максимальная длина строго возрастающего участка: {max_len}")
    print(f"Сумма элементов этого участка: {best_sum}")



