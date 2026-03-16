class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <=1:
            return False
        ans = 0
        for i in range(1, int(math.sqrt(num))+1):
            if num%i ==0:
                ans +=i
                if num//i!=i and num//i != num:
                    ans += num//i
        return ans == num
        