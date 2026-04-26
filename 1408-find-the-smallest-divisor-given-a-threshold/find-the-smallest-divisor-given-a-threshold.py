class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        maxi = max(nums)
        low, high = 1, maxi
        while(low<=high):
            mid = (low+high)//2
            if self.sumByD(nums, mid, len(nums)) <= threshold:
                high = mid-1
            else:
                low = mid+1
        return low

    def sumByD(self, nums, limit, n):
        sum_val = 0
        for num in nums:
            sum_val += math.ceil(num / limit)
        return sum_val     