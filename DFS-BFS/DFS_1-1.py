# 음료수 얼려 먹기 - 깊이우선탐색
n, m = map(int, input().split())

graph = []      # 공간을 그래프로 생각하고 2차원 리스트 생성
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:    # 벗어나면 False
        return False
    if graph[x][y] == 0:    # 방문하지 않은 곳
        graph[x][y] = 1
        
        dfs(x-1, y) # 상 (주변 모두 확인)
        dfs(x+1, y) # 하
        dfs(x, y-1) # 좌
        dfs(x, y+1) # 우
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            count += 1

print(count)