class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int pos=0,neg=0;
        binarySearch(nums,0,nums.size()-1,pos,neg);
        return max(pos,neg);
    }

    void binarySearch(vector<int>&nums, int low, int high, int &pos, int &neg) {
        if(low>high) return;  
        int mid=low+(high-low)/2;
        if(nums[mid]>0) pos++;
        else if(nums[mid]<0) neg++;
        binarySearch(nums,low,mid-1,pos,neg);
        binarySearch(nums,mid+1,high,pos,neg);
    }
};
