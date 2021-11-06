a = [1000, 500, 50, 10, 5, 1]

n = 100
p = [-1 for _ in range(n)]

dp = [-1 for _ in range(n)]
dp[0] = 0

for i in range(n):
    if dp[i] == -1:
        continue

    for s in a:
        nxt = i + s

        if nxt >= n:
            continue

        if dp[nxt] == -1 or dp[nxt] > dp[i] + 1:
            dp[nxt] = dp[i] + 1
            p[nxt] = s

print(dp)
print(p)

value = 47
items = []
while value > 0:
    items.append(p[value])
    value -= p[value]

print(f"{value} =", ' + '.join(map(str, items)))
