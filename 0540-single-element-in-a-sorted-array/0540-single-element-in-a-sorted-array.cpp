class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int a=nums.size()-1;
        if (nums.size()==1) return nums[0];
        int low=1,high=nums.size()-2;
        if (nums[0]!=nums[1]) return nums[0];
        if (nums[a]!=nums[a-1]) return nums[a];
        while(low<=high){
            int mid= low+(high-low)/2;
            if ((nums[mid-1]!=nums[mid]) && (nums[mid]!=nums[mid+1]))return nums[mid];
            else if(mid%2==0){
                if (nums[mid]==nums[mid+1]) low=mid+1;
                else high=mid-1;
            }
            else if (mid%2==1){
                if (nums[mid]==nums[mid-1]) low=mid+1;
                else high=mid-1;
            }
        }
        return -1;
    }
};