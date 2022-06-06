# 큰 수의 법칙 - 풀이1
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

sum = 0
while True:
    for i in range(k):
        if m == 0:
            break
        sum += data[0]
        m -= 1
    if m == 0:
        break
    sum += data[1]
    m -= 1

print(sum)

# 큰 수의 법칙 - 풀이2 (반복되는 수열 이용)
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

count = int(m / (k + 1)) * k
count += m % (k + 1)

sum = 0
sum += (count) * data[0]
sum += (m - count) * data[1]

print(sum)