# 정렬된 배열에서 특정 수의 개수 구하기 - 라이브러리 활용 (Zoho 면접)
from bisect import bisect_left, bisect_right

def count(arr, l_value, r_value):
    l_ind = bisect_left(arr, l_value)
    r_ind = bisect_right(arr, r_value)
    return r_ind - l_ind

n, x = map(int, input().split())
li = list(map(int, input().split()))

result = count(li, x, x)

if result == 0:
    print(-1)
else:
    print(result)

# 다른 방법 - (이진 탐색)
def count_value(arr, n, x):
    a = first(arr, x, 0, n-1)
    if a == None:
        return 0

    b = last(arr, x, 0, n-1)

    return b - a + 1

def first(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if(mid == 0 or target > arr[mid-1]) and arr[mid] == target:
        return mid
    elif arr[mid] >= target:
        return first(arr, target, start, mid-1)
    else:
        return first(arr, target, mid+1, end)

def last(arr, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2
    if(mid == n - 1 or target < arr[mid+1]) and arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return last(arr, target, start, mid-1)
    else:
        return last(arr, target, mid+1, end)

n, x = map(int, input().split())
li = list(map(int, input().split()))

result = count_value(li, n, x)

if result == 0:
    print(-1)
else:
    print(result)