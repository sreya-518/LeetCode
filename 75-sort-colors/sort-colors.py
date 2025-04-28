class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = y = z = 0
        for i in nums:
            if i == 0:
                x += 1
            elif i ==1:
                y +=1
            else:
                z +=1
        nums[0:x] = [0] * x
        nums[x:x+y] = [1] * y
        nums[x+y:x+y+z] = [2] * z
        