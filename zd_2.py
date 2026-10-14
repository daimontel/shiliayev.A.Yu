def rle_encode(s: str) -> str:
    if not s:
        return ""

    result = ""
    count = 1
    length = len(s)

    i = 1
    while i < length:
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
        i += 1

    # Добавляем последнюю группу
    result += s[-1] + str(count)

    return result


# Примеры
print(rle_encode("aaabbc"))   # a3b2c1
print(rle_encode("abcd"))     # a1b1c1d1
print(rle_encode("aaaa"))     # a4
print(rle_encode(""))         # ""
