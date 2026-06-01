class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0

        for r in range(len(prices)):
            if prices[l] > prices[r]:
                l = r

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]
                if profit > max_profit:
                    max_profit = profit

                r += 1

        return max_profit
