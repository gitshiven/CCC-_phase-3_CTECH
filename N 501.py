import math

def binarysearch(arr, n, k):
    l = 0
    h = n - 1
    while l <= h:
        mid = math.floor((l+h)/2)
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            l = mid + 1
        else:
            h = mid - 1
    return 0

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
can = list(map(int, input().split()))

for i in range(m):
    if binarysearch(arr, n, can[i]):
        print("Happy Halloween!")
    else:
        print("Tricky!")
