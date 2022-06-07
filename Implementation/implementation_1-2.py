# 게임 개발
n, m = map(int, input().split())    # 맵 사이즈 입력

d = [[0] * m for _ in range(n)]     # 방문 위치 저장
x, y, dir = map(int, input().split())   # 현재 좌표, 방향 입력
d[x][y] = 1     # 현재 위치 방문 확인

_map = []
for i in range(n):      # 맵 정보 입력
    _map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

def turn_left():    # 0:북 1:동, 2:남, 3:서 / 왼쪽 회전
    global dir      # 변수가 함수 바깥에서 선언된 전역변수이므로 global 사용
    dir -= 1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and _map[nx][ny] == 0:    # 회전 후 이동한 곳이 방문하지 않은 칸 and 육지
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:   # 회전 후 이동한 곳이 방문한 칸 or 바다
        turn_time += 1
    
    if turn_time == 4:      # 네 방향 모두 갈 수 없는 경우
        nx = x - dx[dir]
        ny = y - dy[dir]
        if _map[nx][ny] == 0:   # 뒤에가 육지인 경우 이동
            x = nx
            y = ny
        else:   # 뒤에가 바다인 경우
            break
        turn_time = 0

print(count)