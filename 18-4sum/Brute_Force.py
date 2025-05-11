class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for l in range(k+1, n):
                        if target == nums[i] + nums[j] + nums[k] + nums[l]:
                            temp = [nums[i], nums[j], nums[k], nums[l]]
                            temp.sort()
                            st.add(tuple(temp))
        return [list(items) for items in st]  
