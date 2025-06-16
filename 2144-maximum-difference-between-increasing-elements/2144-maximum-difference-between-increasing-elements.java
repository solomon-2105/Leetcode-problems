class Solution {
    public int maximumDifference(int[] nums) {
        int mini=nums[0];
        int maxDiff=-1;
        for(int i=1;i<nums.length;i++) {
            if(nums[i]>mini){
                maxDiff=Math.max(maxDiff,nums[i]-mini);
            }else{
                mini=nums[i];
            }
        }
        return maxDiff;
    }
}
