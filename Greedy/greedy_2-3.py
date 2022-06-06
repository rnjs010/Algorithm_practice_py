# 문자열 뒤집기
n = input()

first = n[0]
count0 = 0
count1 = 0

for i in range(1, len(n)):
    if first == n[i]:
        continue
    else:
        if n[i-1] == '0':
            count0 += 1
        else:
            count1 += 1
        first = n[i]

if count0 != 0 or count1 != 0:
    if n[-1] == '0':
        count0 += 1
    else:
        count1 +=1

print(min(count0, count1))


# 문자열 뒤집기 - (책 정답code)
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))