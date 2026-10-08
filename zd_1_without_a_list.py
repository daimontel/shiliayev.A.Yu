def task1_without_list():
    try:
        n_str = input("Введите количество чисел N: ")
        n = int(n_str)
        if n <= 0:
            print("N должно быть положительным.")
            return
    except ValueError:
        print("Ошибка ввода N.")
        return

    # Переменные для текущего возрастающего участка
    current_len = 0
    current_sum = 0
    prev_val = None

    # Переменные для лучшего участка
    max_len = 0
    best_sum = 0

    count = 0
    # Читаем числа, пока не наберём N штук (поддерживаем ввод через пробелы)
    while count < n:
        line = input()
        parts = list(map(int, line.split()))  # Это только для парсинга строки, не храним всю последовательность
        for x in parts:
            if count >= n:
                break

            if prev_val is None:
                # Первое число
                current_len = 1
                current_sum = x
            else:
                if x > prev_val:
                    # Продолжаем возрастающий участок
                    current_len += 1
                    current_sum += x
                else:
                    # Участок прервался, проверяем, был ли он лучшим
                    if current_len > max_len:
                        max_len = current_len
                        best_sum = current_sum
                    # Начинаем новый участок с текущего числа
                    current_len = 1
                    current_sum = x

            prev_val = x
            count += 1

    # После цикла проверим последний участок
    if current_len > max_len:
        max_len = current_len
        best_sum = current_sum

    # Если N > 0, но ни одного участка не обновилось (например, N=1)
    if n > 0 and max_len == 0:
        max_len = 1
        # best_sum уже должен быть корректным из последнего участка

    print(f"Максимальная длина строго возрастающего участка: {max_len}")
    print(f"Сумма элементов этого участка: {best_sum}")

# task1_without_list()
