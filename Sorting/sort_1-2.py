# 성적이 낮은 순서로 학생 출력하기 - 기본 정렬 라이브러리 (D 기업 프로그래밍 콘테스트 예선)
n = int(input())

arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr.sort(key=lambda s: s[1])

for student in arr:
    print(student[0], end=' ')