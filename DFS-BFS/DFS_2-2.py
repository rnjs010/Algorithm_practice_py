# 연구소 - (백준 14502)
from itertools import combinations

n, m = map(int, input().split())

graph = []     # 기존 맵
for _ in range(n):
    graph.append(list(map(int, input().split())))

new_map = [[0] * m for _ in range(n)]   # 벽 추가 맵

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

def wall_score():
    result = []     # 벽 생성 경우 별 0의 개수 저장
    
    # 조합이용하여 벽 생성할 곳 정하기
    combi = [(x, y) for x in range(n) for y in range(m) if graph[x][y] == 0]    
    li = list(combinations(combi, 3))

    for i in range(len(li)):    # 벽 3개 가능한 모든 경우 list
        for k in range(n):  # 새로운 맵에 기존 맵 복사
            for j in range(m):
                new_map[k][j] = graph[k][j]

        for j in range(3):  # 벽 생성
            x, y = li[i][j]
            new_map[x][y] = 1

        for a in range(n):  # 바이러스 전파
            for b in range(m):
                if new_map[a][b] == 2:
                    virus(a, b)

        sum = 0
        for k in range(n):  # 오염되지 않은 부분 수
            for j in range(m):
                if new_map[k][j] == 0:
                    sum += 1

        result.append(sum)
    return result

def virus(x, y):    # 모든 방향 바이러스 전파
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if new_map[nx][ny] == 0:
                new_map[nx][ny] = 2
                virus(nx, ny)

print(max(wall_score()))


# 다른 방법 (시간 초과)
# + score함수, 바이러스 함수, 입력 부분
result = 0
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                new_map[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if new_map[i][j] == 2:
                    virus(i, j)
        result = max(result, score())
        return result
        
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1

dfs(0)
print(result)