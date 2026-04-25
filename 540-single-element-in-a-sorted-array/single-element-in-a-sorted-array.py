class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #[1,1,3,5,5,6,6] --> n = 7/2 => 3 ==> left different so on left
        #[1,1,3,3,5,6,6] --> n = 7/2 => 3 ==> right different so on right
        #[1,3,3,5,5] --> n = 5/2 => 2 ==> 
        n = len(nums)
        res = 0
        for num in nums:
            res ^= num
        return res
        