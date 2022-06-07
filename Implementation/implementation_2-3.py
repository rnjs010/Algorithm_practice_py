# 문자열 압축 - (프로그래머스 Lv.2)
def solution(s):
    answer = len(s)
    
    for i in range(1,len(s) // 2 + 1):
        _str = ""
        n_str = s[0:i]
        count = 1
        for j in range(i,len(s),i):
            if n_str == s[j:j+i]:
                count += 1
            else:
                _str += str(count) + n_str if count >= 2 else n_str
                n_str = s[j:j+i]
                count = 1
        _str += str(count) + n_str if count >= 2 else n_str
        answer = min(answer, len(_str))                                
    
    return answer


# li = "abcdabcde"
# for i in range(0,len(li),2): # 끝나는 지점이 문자열 길이보다 길어도 이상 없음
#     print(li[i:i+2])