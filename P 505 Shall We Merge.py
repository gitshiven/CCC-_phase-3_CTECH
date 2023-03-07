def merge_sort_and_count_inversions(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_count = merge_sort_and_count_inversions(arr[:mid])
    right, right_count = merge_sort_and_count_inversions(arr[mid:])
    merged, merged_count = merge_and_count_inversions(left, right)

    return merged, left_count + right_count + merged_count

def merge_and_count_inversions(left, right):
    i, j = 0, 0
    count = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, count

n = int(input())
a = [int(input()) for _ in range(n)]

_, count = merge_sort_and_count_inversions(a)

print(count)
