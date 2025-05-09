class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        countMap = defaultdict(int)
        total = 0
        countMap[0] = 1
        for i in range(n):
            total += nums[i]
            remove  = total - k
            count += countMap[remove]
            countMap[total] +=1     
        return count   