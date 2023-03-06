import math
q=1
l=[int(i) for i in input().split()]
r=l[0]
s=l[1]
t=l[2]
for i in range(r,s,-1):
    q*=i
print(q%t)
