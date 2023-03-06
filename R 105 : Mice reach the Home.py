s = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
 
res = 0
#run in python 3
for i in range(s):
  if abs(a[i] - b[i]) > res: res = abs(a[i] - b[i])
print(res)
