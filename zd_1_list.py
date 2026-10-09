
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

    while len(nums) < n:
        line = input()
        parts = list(map(int, line.split()))
        nums.extend(parts)

    max_len = 0
    best_sum = 0

    i = 0
    while i < n:

        start = i
        current_len = 1
        current_sum = nums[i]


        while i + 1 < n and nums[i + 1] > nums[i]:
            i += 1
            current_len += 1
            current_sum += nums[i]


        if current_len > max_len:
            max_len = current_len
            best_sum = current_sum

        i += 1  

    if max_len == 0 and n > 0:
        max_len = 1
        best_sum = nums[0]

    print(f"Максимальная длина строго возрастающего участка: {max_len}")
    print(f"Сумма элементов этого участка: {best_sum}")



