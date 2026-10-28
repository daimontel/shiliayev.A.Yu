def transform(matrix, rule='max'):

    n = len(matrix)
    if n == 0:
        return []
    m = len(matrix[0])

    # Создаём результирующую матрицу того же размера
    result = [[0.0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            # Собираем все элементы из прямоугольника
            values = []
            for r in range(i + 1):
                for c in range(j + 1):
                    values.append(matrix[r][c])

            if rule == 'max':
                result[i][j] = max(values)
            elif rule == 'min':
                result[i][j] = min(values)
            elif rule == 'avg':
                s = sum(values)
                result[i][j] = s / len(values) if len(values) > 0 else 0.0
            elif rule == 'sum':
                result[i][j] = sum(values)
            else:
                raise ValueError("Неизвестное правило: {}".format(rule))

    return result



if __name__ == "__main__":
    # Ввод двумерного массива: сначала n, m, потом n строк по m чисел
    n, m = map(int, input("Введите размеры массива n m: ").split())
    matrix = []
    print("Введите элементы матрицы (по строкам, числа через пробел):")
    for _ in range(n):
        row = [float(x) for x in input().split()]
        if len(row) != m:
            raise ValueError("Количество элементов в строке не совпадает с m")
        matrix.append(row)

    rules = ['max', 'min', 'avg', 'sum']
    for r in rules:
        transformed = transform(matrix, r)
        print(f"\nПравило '{r}':")
        for row in transformed:
            print(" ".join("{:.2f}".format(x) for x in row))
