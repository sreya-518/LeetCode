class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        visitor = [0] * (10**4+1)
        result = 0
        for num in nums:
            if visitor[num] == 0:
                visitor[num] = 1
                cnt = 0
                for i in range(len(nums)):
                    if num == nums[i]:
                        cnt += 1
                if cnt % k == 0:
                    result += (num * cnt)
        return result







        