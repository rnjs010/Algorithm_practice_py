# 미로 탈출 - 너비우선탐색
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()     # 큐 생성
    queue.append((x,y)) # 현재 위치 넣기

    while queue:    # 큐가 비어 있지 않을 때까지
        x, y = queue.popleft()  # 선입선출
        for i in range(4):  # 모든 방향 확인
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 그래프 벗어난 경우
                continue

            if graph[nx][ny] == 0:  # 장애물이 있는 경우
                continue
            
            if graph[nx][ny] == 1:  # 처음 방문한 노드
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]  # 가장 오른쪽 아래의 값이 최단 거리

print(bfs(0,0))