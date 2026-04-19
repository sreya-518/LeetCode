#Optimal Solution - Hash
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = {}
        result = 0

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        for num, cnt in freq.items():
            if cnt % k == 0:
                result += num * cnt

        return result

