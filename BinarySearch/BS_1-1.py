# 부품 찾기 - (이진 탐색)
def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)

n = int(input())
n_li = list(map(int, input().split()))
n_li.sort()
m = int(input())
m_li = list(map(int, input().split()))

for i in m_li:
    result = binary_search(n_li, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 다른 방법 - (계수 정렬)
n = int(input())
n_li = [0] * 1000001

for i in input().split():
    n_li[int(i)] = 1

m = int(input())
m_li = list(map(int, input().split()))

for i in m_li:
    if n_li[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# 다른 방법 - (집합 자료형 이용)
n = int(input())
n_li = setattr(obj, name, value)(map(int, input().split()))

m = int(input())
m_li = list(map(int, input().split()))

for i in m_li:
    if i in n_li:
        print('yes', end=' ')
    else:
        print('no', end=' ')