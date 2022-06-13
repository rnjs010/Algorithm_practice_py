# 떡볶이 떡 만들기 - (이진 탐색)
n, m = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = max(li)
h = 0

while start<=end:
    sum = 0
    mid = (start+end) // 2
    for x in li:
        if x > mid:
            sum += x - mid
    if sum < m:
        end = mid - 1
    else:
        h = mid
        start = mid + 1

print(h)