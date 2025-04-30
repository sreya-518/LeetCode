#Optimal (O(n log n) time, O(1) space) – if returning elements, not indices
def two_sum_optimal(arr, k):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == k:
            return [arr[left], arr[right]]
        elif s < k:
            left += 1
        else:
            right -= 1
    return []
