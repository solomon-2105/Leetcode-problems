class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int a=0,mid;
        int b=nums.size();
        while(a<b){
            mid=a + ((b-a)/2);
            if(nums[mid]==target){
                return mid;
            }
            else if(nums[mid]<target){
                a=mid+1;
            }
            else{
                b=mid;
            }
    }
        return a;}
};