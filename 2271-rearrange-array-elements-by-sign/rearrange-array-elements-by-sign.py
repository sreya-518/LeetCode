class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        positive = []
        negative = []
        for num in nums:
            if num >= 0 :
                positive.append(num)
            else:
                negative.append(num)
        i = 0
        j=0
        while i < n:
            nums[i] = positive[j]
            nums[i+1] = negative[j]
            j += 1
            i +=2
        return nums