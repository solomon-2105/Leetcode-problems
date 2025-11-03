class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0] 
        profit=0
        for i in prices:
            if i<mini:
                mini=i
            if profit<(i-mini):
                profit=i-mini
        return profit