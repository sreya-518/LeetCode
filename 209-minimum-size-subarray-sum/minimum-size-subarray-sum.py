class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #Better Sol
        left = 0
        right = len(nums) - 1
        Total = 0
        minLen = float('inf')
        for right in range(len(nums)):
            Total += nums[right]
            while Total >= target:
                length = right - left + 1
                minLen = min(length, minLen)
                Total = Total - nums[left]
                left += 1
        return 0 if minLen == float('inf') else minLen