class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            #Brute Force: Check from i=0 to n-1 and j=i+1 to n.
            # TC - O(N^2) SC - O(1)
            # Better Solution: HashMap
            TwoSumMap = {}

            for i, n in enumerate(nums):
                diff = target - n
                if diff in TwoSumMap:
                    return [TwoSumMap[diff], i]
                TwoSumMap[n] = i

            

            

        