import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans = n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
# can also use --> bisect.bisect_left(nums, target)
