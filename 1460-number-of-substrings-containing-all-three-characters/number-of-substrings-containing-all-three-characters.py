class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        dictionary = {'a': -1, 'b': -1, 'c': -1}
        for i in range(len(s)):
            dictionary[s[i]] = i
            if dictionary['a']!=-1 and dictionary['b']!=-1 and dictionary['c']!=-1:
                minimum = min(dictionary['a'], dictionary['b'], dictionary['c'])
                count += minimum + 1
        return count



        