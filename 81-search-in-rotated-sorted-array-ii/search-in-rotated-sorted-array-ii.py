class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        #Time Complexity - Average & Best Case - O(log N)
        #Worst Case - O(N/2)
        n = len(nums)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return True
            
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low = low + 1
                high = high - 1
                continue
            
            if nums[low] <= nums[mid]:
                if nums[low]<=target and nums[mid]>=target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and nums[high] >= target:
                    low = mid + 1
                else:
                    high = mid - 1         
        return False
            