class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        result = 0

        left_pointer = 0
        for right_pointer in range(1, len(prices)):
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer
            result = max(result, prices[right_pointer] - prices[left_pointer])
        return result


prices = [7, 1, 5, 3, 6, 4]
test = Solution()
max_profit = test.maxProfit(prices)
print(max_profit)
