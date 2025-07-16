class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        r = k-1
        currSum = sum(nums[:k])/k
        maxSum = currSum
        while(r<len(nums)-1):
            currSum -= (nums[l]/k)
            l += 1
            r += 1
            currSum += (nums[r]/k)
            maxSum = max(maxSum, currSum)
        return maxSum

        