class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Optimal Solution
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, n):
                if j!=i+1 and nums[j] == nums[j-1]: continue
                k = j+1
                l = n-1
                while(k < l):
                    _sum = nums[i] + nums[j] + nums[k] + nums[l] 
                    if _sum > target: l -= 1
                    elif _sum < target: k += 1
                    else:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        ans.append(temp)  
                        k += 1
                        l -= 1
                        while(k < l and nums[k]==nums[k-1]): k += 1
                        while(k < l and nums[l]==nums[l+1]): l -= 1 
        return ans
