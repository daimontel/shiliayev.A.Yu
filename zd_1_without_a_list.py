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

    current_len = 0
    current_sum = 0
    prev_val = None

    max_len = 0
    best_sum = 0

    count = 0
    while count < n:
        line = input()
        parts = list(map(int, line.split()))  # Это только для парсинга строки, не храним всю последовательность
        for x in parts:
            if count >= n:
                break

            if prev_val is None:
           
                current_len = 1
                current_sum = x
            else:
                if x > prev_val:
                 
                    current_len += 1
                    current_sum += x
                else:
                    if current_len > max_len:
                        max_len = current_len
                        best_sum = current_sum
                    current_len = 1
                    current_sum = x

            prev_val = x
            count += 1

    if current_len > max_len:
        max_len = current_len
        best_sum = current_sum

    if n > 0 and max_len == 0:
        max_len = 1

    print(f"Максимальная длина строго возрастающего участка: {max_len}")
    print(f"Сумма элементов этого участка: {best_sum}")

# task1_without_list()
