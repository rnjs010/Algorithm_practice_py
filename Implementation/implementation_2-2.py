# 문자열 재정렬
S = input()

alpha = []
num = 0

for i in range(len(S)):
    if S[i].isalpha():      # 확인할값.isalpha() : 문자열에 숫자 및 공백이 있으면 False / 값.isdigit() : 문자 및 기호가 있으면 False
        alpha.append(S[i])
    else:
        num += int(S[i])

alpha.sort()

if num != 0:
    alpha.append(str(num))

print(''.join(alpha))