def max_experience(levels, experience):
    dp = [[0] * (i + 1) for i in range(levels)]

    for j in range(levels):
        dp[levels - 1][j] = experience[levels - 1][j]

    for i in range(levels - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = experience[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]

with open("career.in", "r") as file:
    levels = int(file.readline())
    experience = [list(map(int, file.readline().split())) for _ in range(levels)]

result = max_experience(levels, experience)
with open("career.out", "w") as file:
    file.write(str(result))
