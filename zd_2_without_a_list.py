def task2_without_list():
    try:
        n_str = input("Введите количество чисел N: ")
        n = int(n_str)
        if n < 4:
            print("Для задачи требуется минимум 4 числа.")
            return
    except ValueError:
        print("Ошибка ввода N: введите целое число.")
        return

    a = b = c = d = None
    count = 0

    max_sum = None
    best_pos = -1

    while count < n:
        try:
            line = input()
        except EOFError:

            break

        parts = line.split()
        if not parts:
            continue  
        for token in parts:
            if count >= n:
                break
            try:
                x = int(token)
            except ValueError:
                print(f"Ошибка: '{token}' не является целым числом. Пропущено.")
                continue

            a, b, c, d = b, c, d, x
            count += 1

            if count >= 4:
                window_sum = a + b + c + d
                pos = count - 3
                if max_sum is None or window_sum > max_sum:
                    max_sum = window_sum
                    best_pos = pos

    if count < 4:
        print(f"Недостаточно чисел: введено {count}, требуется минимум 4.")
        return

    if max_sum is None:
        print("Не удалось найти группу из 4 чисел: недостаточно корректных данных.")
    else:
        print(f"Наибольшая сумма из 4 подряд идущих чисел: {max_sum}")
        print(f"Позиция первого элемента этой группы: {best_pos}")

# task2_without_list()
