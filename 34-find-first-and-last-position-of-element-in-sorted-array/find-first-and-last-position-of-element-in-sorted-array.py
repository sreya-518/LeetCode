from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def lowerBound(arr, x):
            low, high = 0, len(arr) - 1
            ans = len(arr)
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def upperBound(arr, x):
            low, high = 0, len(arr) - 1
            ans = len(arr)
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] > x:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ans

        def firstAndLastPosition(arr, x):
            first = lowerBound(arr, x)
            last = upperBound(arr, x)
            if first == len(arr) or arr[first] != x:
                return [-1, -1]
            return [first, last - 1]

        return firstAndLastPosition(nums, target)