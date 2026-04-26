#Linear Search
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        length = len(bloomDay)
        mini, maxi = min(bloomDay), max(bloomDay)
        if m*k>length:
            return -1
        while(mini<=maxi):
            mid = (mini+maxi)//2
            if self.func(bloomDay, mid, m, k) == True:
                maxi = mid - 1
            else:
                mini = mid+1
        return mini
                
                
        
    def func(self, nums, i, m, k):
        cnt = 0
        noOfBouquets = 0
        for num in nums:
            if num <= i:
                cnt += 1
            else:
                noOfBouquets += (cnt//k)
                cnt = 0
        noOfBouquets += (cnt//k)
        return noOfBouquets >= m
            