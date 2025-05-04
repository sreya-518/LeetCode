class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nonZero = 0
        for num in nums:
            if num != 0:
                nums[nonZero] = num
                nonZero +=1
        for i in range(nonZero, len(nums)):
            nums[i] = 0