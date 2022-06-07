# 럭키 스트레이트 - (백준 18406)
score = input()

half = len(score) // 2
l = score[:half]
r = score[half:]

l_score = 0
r_score = 0
for i in range(half):
    l_score += int(l[i])
    r_score += int(r[i])

if l_score == r_score:
    print("LUCKY")
else:
    print("READY")
