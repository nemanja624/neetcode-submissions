class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
            else:
                profit = prices[right] - prices[left]
                if profit > max_profit:
                    max_profit = profit

          

        return max_profit

