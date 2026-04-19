class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        longest = 1
        s = set(nums)
        for num in s:
            if num-1 not in s:
                cnt = 1
                x = num
                while x+1 in s:
                    cnt += 1
                    x += 1
                longest = max(longest, cnt)
        return longest


        