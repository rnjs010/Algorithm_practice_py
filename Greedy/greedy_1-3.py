# 1이 될 때까지 - 풀이1
n, k = map(int, input().split())
count = 0

while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else:
        n -= 1
        count += 1

print(count)

# 1이 될 때까지 - 풀이2 (효율적인 방식)
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)