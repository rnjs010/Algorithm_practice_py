# 특정 거리의 도시 찾기 - 너비우선탐색 (백준 18352)
from collections import deque
import sys  # PyPy3에서는 없어도 O, Python3에서는 없으면 시간초과
f = sys.stdin.readline

n, m, k, x = map(int, f().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)  # 노드별 연결된 노드들

dis = [-1] * (n+1)
dis[x] = 0 

def bfs(x):
    q = deque([x])
    while q:
        now = q.popleft()
        for next_n in graph[now]:
            if dis[next_n] == -1:   # 방문하지 않은 노드
                dis[next_n] = dis[now] + 1
                q.append(next_n)

    if k not in dis:
        print(-1)
    else:
        result = list(filter(lambda i: dis[i] == k, range(len(dis))))
        for i in range(len(result)):
            print(result[i])

bfs(x)