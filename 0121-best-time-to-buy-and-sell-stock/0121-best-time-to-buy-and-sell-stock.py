class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # mp=0
        # for i in range(1,len(prices)):
        #     if prices[i]>prices[i-1]:
        #         mp=mp+(prices[i]-prices[i-1])
        # return mp

        # mini=min(prices)
        # index=0
        # for i in range(len(prices)):
        #     if prices[i]==mini:
        #         index=i
        #         break
        # maxii=max(prices[index:])
        # return maxii-mini
        n=len(prices)
        buy,sell,profit,maxprofit=prices[0],prices[0],0,0
        for i in range(1,n):
            if prices[i]<buy:
                buy=prices[i]
                continue
            else:
                sell=prices[i]
            profit=sell-buy
            maxprofit=max(profit,maxprofit)
        return maxprofit







