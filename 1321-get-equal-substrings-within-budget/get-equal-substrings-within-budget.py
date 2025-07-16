class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l, r = 0, 0
        maxLen = 0
        cost = 0
        while(r<len(s)):
            cost += abs(ord(s[r]) - ord(t[r]))
            if(cost>maxCost):
                cost -= abs(ord(s[l]) - ord(t[l]))
                l = l+1
            if(cost<=maxCost):
                maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen



        