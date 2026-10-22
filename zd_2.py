def lps_length(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):          # длина подстроки
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


def lps_string(s):

    n = len(s)
    if n == 0:
        return ""
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])


    left, right = [], []
    i, j = 0, n - 1
    while i <= j:
        if i == j:
            left.append(s[i])
            break
        if s[i] == s[j]:
            left.append(s[i])
            right.append(s[j])
            i += 1
            j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    return "".join(left + right[::-1])


# Проверка на примерах из условия
if __name__ == "__main__":
    for s in ["bbbab", "cbdb", "a", "", "abba", "abcde"]:
        print(f"{s!r:8} -> длина {lps_length(s)}, LPS = {lps_string(s)!r}")
