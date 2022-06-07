# 왕실의 나이트
pos = input()
row = int(pos[1])
col = ord(pos[0]) - ord('a') + 1  # ord(문자) : 해당 문자에 대한 유니코드 정수 반환 ord('a') = 97

m_dir= [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2)] # 움직일 수 있는 방향

count = 0
for m_dir in m_dir:
    n_row = row + m_dir[0]
    n_col = col + m_dir[1]
    if n_row >= 1 and n_row <= 8 and n_col >= 1 and n_col <= 8: # 이동 가능한 위치
        count += 1

print(count)