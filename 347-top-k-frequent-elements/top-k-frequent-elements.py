class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Sorting - O(N log N + N) SP - O(1)
        #HashMap - TC:O(N + N log N) SP: O(N)
        #BucketSort
        count = {}
        frequency = [[] for i in range(len(nums)+1)]
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, c in count.items():
            frequency[c].append(n)

        result = []
        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                result.append(j)
                if len(result) == k:
                    return result


