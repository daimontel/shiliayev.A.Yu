a = b = c = None  
global_min = None     

print("Вводите числа по одному. Введите 'q' для завершения.")
print("Программа хранит последние 3 числа, считает минимум внутри тройки и сохраняет лучший результат за всё время.")

while True:
    user_input = input("Число: ").strip()
    
    if user_input.lower() in ('q', 'quit'):
        break
    
    if not user_input:
        print("Пустой ввод игнорируется. Введите число или 'q'.")
        continue
    
    try:
        current = int(user_input)
    except ValueError:
        print("Пожалуйста, введите целое число или 'q' для выхода.")
        continue

    a, b, c = b, c, current

    vals = [x for x in (a, b, c) if x is not None]

    if len(vals) >= 2:
        local_min = None
        for i in range(len(vals)):
            for j in range(i + 1, len(vals)):
                diff = abs(vals[i] - vals[j])
                if local_min is None or diff < local_min:
                    local_min = diff
        

        if global_min is None or local_min < global_min:
            global_min = local_min

if global_min is not None:
    print("Лучшая (минимальная) разница, найденная среди любых троек за всё время:", global_min)
else:
    print("Было введено меньше двух чисел — нельзя найти разницу.")
