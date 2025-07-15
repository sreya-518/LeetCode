class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        maxSum = 0
        cardSum = sum(cardPoints[:k])
        maxSum = cardSum

        for i in range(1, k+1):
            cardSum = cardSum + cardPoints[-i] - cardPoints[k-i]
            maxSum = max(maxSum, cardSum)
        return maxSum
  