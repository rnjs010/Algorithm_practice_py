# 안테나 - (백준 18310)
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
print(arr[(n-1)//2])