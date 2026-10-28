from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")]+=1
            anagramMap[tuple(count)].append(s)
        return list(anagramMap.values())
    

        # anagram_map = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26
        #     for c in word:
        #         count[ord(c) - ord("a")] += 1

        #     key = tuple(count)
        #     anagram_map[key].append(word)
        # return list(anagram_map.values())