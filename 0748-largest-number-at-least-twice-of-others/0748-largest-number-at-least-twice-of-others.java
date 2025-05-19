class Solution {
    public int dominantIndex(int[] nums) {
        int maxi=Integer.MIN_VALUE , index=-1;
        for (int i=0;i<nums.length;i++){
            if (nums[i]>maxi){
                index=i;
                maxi=nums[i];
        }}
        for (int i=0;i<nums.length;i++){
            if (nums[i]==maxi) continue;
            if ((nums[i]*2)>maxi) return -1;
        }
        return index;
    }
}