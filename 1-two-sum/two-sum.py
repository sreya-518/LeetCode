class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            #Brute Force: Check from i=0 to n-1 and j=i+1 to n.
            # TC - O(N^2) SC - O(1)
            # Better Solution: HashMap
            difference = {}
            for i in range(len(nums)):
                diff = target - nums[i]
                if diff in difference:
                    return [difference[diff],i]
                else:
                    difference[nums[i]] = i 

            

        