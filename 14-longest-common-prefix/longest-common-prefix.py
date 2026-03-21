class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #Start with the first word as the prefix and keep shortening it until it matches the beginning of every other word.
        res = ""
        prefix = strs[0]
        for s in strs[1:]: 
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

        return prefix

        
        