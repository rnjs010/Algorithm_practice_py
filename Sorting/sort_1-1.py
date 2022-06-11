# 위에서 아래로 - 기본 정렬 라이브러리 (T 기업 코딩 테스트)
n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in arr:
    print(i, end=' ')