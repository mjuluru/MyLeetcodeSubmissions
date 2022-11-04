class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        pos = 0
        for i in range(1,len(prices)):
            if profit < (prices[i] - prices[pos]):
                profit = prices[i] - prices[pos]
            elif prices[i] < prices[pos]:
                pos = i
        return profit
