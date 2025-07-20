class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, mini= 0, prices[0]
        for i in range(1,len(prices)):
            brr=prices[i]-mini
            profit=max(profit , brr)
            mini=min(mini,prices[i])
        return profit