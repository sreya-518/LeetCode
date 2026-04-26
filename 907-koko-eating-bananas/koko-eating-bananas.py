#Optimal
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi = max(piles)
        low, high = 1, maxi
        while(low<=high):
            mid = (low+high)//2
            reqtime = self.totaltime(piles, mid)
            if reqtime <= h:
                high = mid-1
            else:
                low = mid+1
        return low

    def totaltime(self, piles, i):
        sum_val = 0
        for num in piles:
            sum_val += math.ceil(num/i)
        return sum_val