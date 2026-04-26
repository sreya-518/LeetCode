#Similar to Agressive Cows - Binary Search on Answers
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        low, high = 1, position[-1] - position[0]
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            if self.func(position, m, mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1 
        return ans         

    def func(self, position, m, distance):
        cnt = 1
        last = position[0]
        for i in range(1, len(position)):
            if (position[i] - last) >= distance:
                cnt+=1
                last = position[i]
                if cnt >= m:
                    return True
        return False

            