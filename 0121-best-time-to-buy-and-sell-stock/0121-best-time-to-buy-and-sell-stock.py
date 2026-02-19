class Solution:
    def maxProfit(self, p: List[int]) -> int:
        # m stores the minimum price seen so far (best day to buy).
        # profit stores the maximum profit found so far.
        
        profit = 0
        m = p[0]
        
        for i in range(1, len(p)):
            # If current price is higher than the minimum price,
            # calculate profit if we sell today.
            if m < p[i]:
                profit = max(profit, p[i] - m)
            
            # If current price is lower than minimum price,
            # update minimum price (better day to buy).
            else:
                m = p[i]
        
        # Return the maximum profit possible.
        return profit