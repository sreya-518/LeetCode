class Solution:
    def isPalindrome(self, s: str) -> bool:
        # res = []
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         res.append(s[i].lower())
        # l, r = 0, len(res)-1
        # while(l<r):
        #     if res[l] == res[r]:
        #         l += 1
        #         r-=1
        #     else:
        #         return False
        # return True
        # while going only convetr and go
        l, r = 0, len(s) - 1

        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[r] != s[l]:
                return False
            
            l, r = l + 1, r - 1
        
        return True