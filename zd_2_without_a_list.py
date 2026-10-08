def task2_without_list():
    try:
        n_str = input("Введите количество чисел N: ")
        n = int(n_str)
        if n < 4:
            print("Для задачи требуется минимум 4 числа.")
            return
    except ValueError:
        print("Ошибка ввода N.")
        return

    a = b = c = d = None  # Последние 4 числа
    count = 0

    max_sum = None
    best_pos = -1

    while count < n:
        line = input()
        parts = list(map(int, line.split()))  # Только парсинг строки, не хранение всей последовательности
        for x in parts:
            if count >= n:
                break

            # Сдвигаем окно
            a, b, c, d = b, c, d, x
            count += 1

            # Когда у нас есть 4 числа (count >= 4), можно считать сумму
            if count >= 4:
                window_sum = a + b + c + d
                pos = count - 3  # Позиция первого элемента в окне (1-индексация)
                if max_sum is None or window_sum > max_sum:
                    max_sum = window_sum
                    best_pos = pos

    print(f"Наибольшая сумма из 4 подряд идущих чисел: {max_sum}")
    print(f"Позиция первого элемента этой группы: {best_pos}")

# task2_without_list()
