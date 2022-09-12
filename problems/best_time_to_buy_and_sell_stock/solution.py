class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        diff = 0
        for i in prices[1:]:
            if i < buy:
                buy = i
            elif i > buy and diff < (i-buy):
                diff = i-buy
        return diff
            
        