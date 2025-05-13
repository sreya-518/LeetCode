class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def BinarySearch(nums, target):
            for i in range(len(nums)):
                if nums[i] == target:
                    return True
            return False
        return BinarySearch(nums, target)