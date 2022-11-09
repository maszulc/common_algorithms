class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            result = max(result, prices[r] - prices[l])
        return result
        