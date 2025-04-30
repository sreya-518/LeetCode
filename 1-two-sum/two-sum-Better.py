#Better (O(n log n) time with sorting, or O(n) time with hashing; O(n) space)
def two_sum_better(arr, k):
    hashmap = {}
    for i, num in enumerate(arr):
        diff = k - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []
