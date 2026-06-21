class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0 
        maxProfit = float('-inf')

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                difference = prices[right] - prices[left]
                maxProfit = max(maxProfit, difference)

            #update the window size

        return maxProfit