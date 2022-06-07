# 자물쇠와 열쇠 (완전 탐색) - (프로그래머스 Lv.3)
def turn_matrix_90(a):  # 행렬(리스트) 90도 회전⭐
    n = len(a)
    m = len(a[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

def check(new_lock):    # 새 자물쇠 중간 부분 1인지 확인
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n*3) for _ in range(n*3)]    # 기존 자물쇠의 3배 크기 생성
    
    for i in range(n):      # 새 자물쇠 중앙에 기존 자물쇠 넣기
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for all_dir in range(4):     # 모든 방향, 위치 확인
        key = turn_matrix_90(key)

        for x in range(n*2):
            for y in range(n*2):

                for i in range(m):      # 키 넣기
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:     # 확인
                    return True

                for i in range(m):      # 키 빼기
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False