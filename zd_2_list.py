def task2_with_list():
    try:
        n = int(input("Введите количество чисел N: "))
        if n < 4:
            print("Для задачи требуется минимум 4 числа.")
            return
    except ValueError:
        print("Ошибка ввода N.")
        return

    nums = []
    print(f"Введите {n} целых чисел:")
    while len(nums) < n:
        line = input()
        parts = list(map(int, line.split()))
        nums.extend(parts)

    max_sum = None
    best_pos = -1  
    for i in range(n - 3):
        window_sum = sum(nums[i:i+4])
        if max_sum is None or window_sum > max_sum:
            max_sum = window_sum
            best_pos = i + 1  # Переводим в 1-индексацию

    print(f"Наибольшая сумма из 4 подряд идущих чисел: {max_sum}")
    print(f"Позиция первого элемента этой группы: {best_pos}")

# task2_with_list()
