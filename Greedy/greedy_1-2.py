# 숫자 카드 게임 - 풀이1 (2중 반복문 이용)
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))  # 행 한 줄 입력 받기
    min_data = 10001
    for j in data:  # 하나의 행 중 가장 작은 수 찾기
        min_data = min(min_data, j)
    result = max(result, min_data) # 가장 작은 수들 중 가장 큰 수 찾기

print(result)

# 숫자 카드 게임 - 풀이2
n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_data = min(data)
    result = max(result, min_data)

print(result)