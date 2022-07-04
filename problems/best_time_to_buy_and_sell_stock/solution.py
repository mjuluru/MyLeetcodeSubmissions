class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        bp = prices[0]
        for i in prices[1:]:
            if i<bp:
                bp = i
            elif (i-bp) > profit:
                profit = i-bp
        return profit
        
        