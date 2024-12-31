class Solution(object):
    def finalPrices(self, prices):
        new_prices = prices
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    new_prices[i] -= prices[j]
                    break 

        return new_prices  