class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i].isalnum():
                res.append(s[i].lower())
        l, r = 0, len(res)-1
        while(l<r):
            if res[l] == res[r]:
                l += 1
                r-=1
            else:
                return False
        return True