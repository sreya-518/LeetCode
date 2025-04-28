class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Moore’s Voting Algorithm
        count = 0
        for i in range(len(nums)):
            if count == 0:
                count = 1
                element = nums[i]
            elif element == nums[i]:
                count += 1
            else:
                count -= 1
        count1 = 0
        for j in range(len(nums)):
            if element == nums[j]:
                count1 +=1
        if count1 > len(nums)/2:
            return element
        