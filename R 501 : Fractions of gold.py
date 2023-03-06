#This Solution by CHATGPT 1000% success
n, w = map(int, input().split())

samples = []
for i in range(n):
    wi, vi = map(int, input().split())
    samples.append((wi, vi))

samples.sort(key=lambda x: x[1]/x[0], reverse=True)

value = 0
for wi, vi in samples:
    if w == 0:
        break
    fraction = min(w, wi)
    value += fraction * (vi/wi)
    w -= fraction

if w > 0:
    print(-1)
else:
    print(value)
