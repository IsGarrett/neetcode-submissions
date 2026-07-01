class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        sell = 1
        ans = 0

        while sell < (len(prices)) and buy < (len(prices)):
            if prices[buy] <= prices[sell]:
                profit = prices[sell] - prices[buy]
                sell += 1
                if profit > ans:
                    ans = profit
            else:
                buy = sell
                sell += 1
                

        return ans
        