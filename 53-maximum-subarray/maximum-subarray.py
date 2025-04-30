class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        subSum = 0
        for num in nums:
            subSum += num
            maximum = max(subSum, maximum)
            if subSum < 0:
                subSum = 0
        return maximum

