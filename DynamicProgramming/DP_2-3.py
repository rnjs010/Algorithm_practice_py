# 퇴사 - (백준 14501)
n = int(input())
t_li = []
p_li = []
for _ in range(n):
    t, p = map(int, input().split())
    t_li.append(t)
    p_li.append(p)

dp = [0] * (n+1)
max_p = 0

for i in range(n-1, -1, -1):
    time = i + t_li[i]
    if time <= n:
        dp[i] = max(p_li[i] + dp[time], max_p)
        max_p = dp[i]
    else:
        dp[i] = max_p

print(max_p)