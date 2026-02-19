class Solution:
    def maxProfit(self, p: List[int]) -> int:
        # 7 , 1 , 5 , 3 , 6 , 4
        # whenever u come across a better deal, 
        # that is when the price u brought at x day is higher than the current price , we buy in the current day , and look for higher prices in the future days
        profit = 0
        m = p[0]
        for i in range(1 , len(p)):
            if m < p[i] :
                profit = max ( profit , p[i] - m)
            else:
                m = p[i]
        return profit