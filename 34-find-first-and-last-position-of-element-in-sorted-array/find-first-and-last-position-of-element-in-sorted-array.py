import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # i = bisect.bisect_left(nums, target)
        # j = bisect.bisect_right(nums, target)
        # if i == j:
        #     return [-1, -1]
        # return [i, j-1]

        def firstOccurrence(arr, n, k):
            low = 0
            high = n - 1
            first = -1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    first = mid
                    high = mid - 1
                elif arr[mid] < k:
                    low = mid + 1 
                else:
                    high = mid - 1 
            return first


        def lastOccurrence(arr, n, k):
            low = 0
            high = n - 1
            last = -1

            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == k:
                    last = mid
                    low = mid + 1
                elif arr[mid] < k:
                    low = mid + 1 
                else:
                    high = mid - 1

            return last

        def firstAndLastPosition(nums, n, k):
            first = firstOccurrence(nums, n, k)
            if first == -1:
                return (-1, -1)
            last = lastOccurrence(nums, n, k)
            return (first, last)
            
        n = len(nums)
        first, last = firstAndLastPosition(nums, n, target)
        if first == -1:
            return [-1, -1]
        return [first, last]