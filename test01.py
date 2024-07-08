def min_deletions_to_remove_palindromes(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # 初始化单字符的情况
    for i in range(n):
        dp[i][i] = 1

    # 从底向上计算dp值
    for length in range(2, n + 1):  # 子串长度从2到n
        for i in range(n - length + 1):
            j = i + length - 1  # 计算右边界
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] if i + 1 <= j - 1 else 1
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    return dp[0][n - 1]


# 示例
s = "tvuvv"
min_deletions_to_remove_palindromes(s)
