class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = 0
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_price = max(max_price, profit)
        return max_price