def MaxBinaryStringLen(n, arr):
    left = right = ans = count = 0
    while right < n:
        if arr[right] == 1:
            count += 1
            right += 1
        else:
            ans = max(ans, count)
            count = 0
            right += 1
            left = right
    return max(ans, count)

n = int(input())
arr = list(map(int, input().split()))
print(MaxBinaryStringLen(n, arr))
