class Solution {
    public int splitArray(int[] nums, int k) {
        if (nums.length<k) return -1;
        int low=-1,high=0;
        for(int i:nums){
            low=Math.max(low,i);
            high+=i;
        }
        while (low<=high){
            int mid=low+(high-low)/2;
            int c=Bina(nums,mid);
            if (c>k) low=mid+1;
            else high=mid-1;
        }
        return low;
    }

    public int Bina(int[] a, int b){
        int s=1,pages=0;
        for(int i: a){
            if ((pages+i)>b){
                s+=1;
                pages=i;
            }
            else pages+=i;
        }
        return s;
    }
}