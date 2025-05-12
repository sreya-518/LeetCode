import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect.bisect_left(nums, target)
        j = bisect.bisect_right(nums, target)
        if i == j:
            return [-1, -1]
        return [i, j-1]        