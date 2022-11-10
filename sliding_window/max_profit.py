'''
Best Time to Buy and Sell Stock
    - You are given an array prices where prices[i] is the price of a given stock on the ith day.
    - You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    - Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''


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
