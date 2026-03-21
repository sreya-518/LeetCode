from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        #Bucket Sort

        # Step 1: Count frequency of each character
            #freq{t:1, r:1, e:2}
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0)+1
        
        # Step 2: Create buckets (index = frequency)
        bucket = [[] for _ in range(0, len(s)+1)]
        for ch, count in freq.items():
            bucket[count].extend(ch)

        # Step 3: Build result string
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for ch in bucket[i]:
                result.append(ch * i)

        return "".join(result)

        

        



        