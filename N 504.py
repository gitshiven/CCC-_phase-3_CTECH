from bisect import bisect_right

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()

for bj in b:
    i = bisect_right(a, bj)
    print(i, end=' ')
