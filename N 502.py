n = int(input())
a = list(map(int, input().split()))
k = int(input())

# Sort the array in non-decreasing order
a.sort()

# Count the number of pairs (i, j) such that a[i] + a[j] = K
count = 0
for i in range(n):
    complement = k - a[i]
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == complement:
            count += 1
            break
        elif a[mid] < complement:
            left = mid + 1
        else:
            right = mid - 1

# Print the TwoSum value
print(count)
