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
        l = 0
        r = len(s)-1
        while(l<r):
            while l<r and not s[l].isalnum():
                l += 1
            while l<r and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower() and r>-1:
                l += 1
                r -= 1
            else:
                return False
        return True

