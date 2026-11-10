class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        curr = prices[0]

        for p in prices:
            maxProfit = max(maxProfit, p - curr)
            curr = min(p, curr)

        return maxProfit