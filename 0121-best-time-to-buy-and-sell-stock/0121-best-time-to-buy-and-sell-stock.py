class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)  # Keep track of the minimum price so far
            potential_profit = price - min_price  # Calculate the potential profit from the current price
            max_profit = max(max_profit, potential_profit)  # Update the max profit if a higher profit is found

        return max_profit