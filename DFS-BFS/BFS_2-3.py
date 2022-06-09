# 경쟁적 전염 - 너비우선탐색 (백준 18405)
from collections import deque

n, k = map(int, input().split())

graph = []  # 전체 맵
k_li = []   # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:    # 바이러스가 존재하는 경우
            k_li.append((graph[i][j], 0, i, j)) # 바이러스 종류, 시간, 위치

k_li.sort() # 낮은 번호부터 증식

s, x, y = map(int, input().split())

dx = [-1, 1, 0, 0]  # 상 하 좌 우
dy = [0, 0, -1, 1]

q = deque(k_li) # 바이러스 정보 큐에 넣기
while q:
    virus, sec, pos_x, pos_y = q.popleft()
    if sec == s:    # 시간이 되면 종료
        break

    for i in range(4):  # 모든 방향 증식
        nx = pos_x + dx[i]
        ny = pos_y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:   # 맵 범위 내
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, sec+1, nx, ny))

print(graph[x-1][y-1])