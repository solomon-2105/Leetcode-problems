class Solution {
    public int maxProfit(int[] prices) {
        int mini=prices[0];
        int profit=0;
        for(int i=1;i<prices.length;i++){
            if(prices[i]>mini){
                profit=Math.max(profit,prices[i]-mini);
            }
            else{
                mini=prices[i];
            }
        }
        return profit;
    }
}