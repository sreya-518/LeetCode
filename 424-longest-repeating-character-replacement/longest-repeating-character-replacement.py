class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #AABABBA K=1
        #1. total length - most freuent = change
        #change<=k then we have to change Maxlen

        l, r, max_len, max_count = 0, 0, 0, 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_count = max(max_count, count[s[r]])
            if (r - l + 1) - max_count > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len
            






        

        