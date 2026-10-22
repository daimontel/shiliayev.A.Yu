def flatten_one(lst):
    return [x for sub in lst for x in (sub if isinstance(sub, list) else [sub])]
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))   # рекурсивно
        else:
            result.append(item)
    return result


# Проверка
if __name__ == "__main__":
    tests = [
        [1, [2, 3], [4, [5, 6]], 7],
        [[1], [2, [3, [4, [5]]]]],
        [],
        [1, 2, 3],
        [[[], []], [1]],
    ]
    for t in tests:
        print(t, "->", flatten(t))
