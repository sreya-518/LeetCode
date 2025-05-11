class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        st = set()
        for i in range(n):
            for j in range(i+1, n):
                hashSet = set()
                for k in range(j+1, n):
                    total = nums[i] + nums[j] + nums[k]
                    fourth = target - total
                    if fourth in hashSet:
                        temp = [nums[i], nums[j], nums[k], fourth]
                        temp.sort()
                        st.add(tuple(temp))
                    hashSet.add(nums[k])
        return [list(items) for items in st]
