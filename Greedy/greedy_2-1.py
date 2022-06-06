# 모험가 길드
n = int(input())
data = list(map(int, input().split()))
count = 0
data.sort()

people = 0
for i in range(n):
    people += 1
    if people >= data[i]:
        count += 1
        people = 0

print(count)