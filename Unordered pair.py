# Reading input values
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Initializing frequency array
freq = [0]*k


for i in range(n):
    freq[a[i] % k] += 1


count = 0


for r1 in range(1, k//2 + 1):
    r2 = k - r1
    if r1 != r2:
        count += freq[r1] * freq[r2]
    else:
        count += (freq[r1] * (freq[r1]-1)) // 2

count += (freq[0] * (freq[0]-1)) // 2

# Printing the result
print(count)
