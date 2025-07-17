class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        maxlength = 0
        dictionary = {}
        while(r<len(fruits)):
            dictionary[fruits[r]] = dictionary.get(fruits[r], 0)+1
            if len(dictionary) > 2:
                dictionary[fruits[l]] = dictionary.get(fruits[l]) - 1
                if dictionary[fruits[l]] == 0:
                    del dictionary[fruits[l]]
                l += 1
            elif len(dictionary) <= 2:
                maxlength = max(maxlength, r-l+1)
            r+=1
        return maxlength



        