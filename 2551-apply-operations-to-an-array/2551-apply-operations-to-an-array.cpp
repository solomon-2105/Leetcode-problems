class Solution {
public:
    vector<int> applyOperations(vector<int>& nums) {
        int i=0;
        int j=i+1;
        while (i<nums.size()-1){
            if (j<nums.size() && nums[i]==nums[j]){
                nums[i]*=2;
                nums[j]=0;
            }
            i++;
            j++;
        }Move_zeroes(nums);
        return nums;
    }
    
    void Move_zeroes(vector<int> &nums){
        int i=0;
        for(int j=0;j<nums.size();j++){
            if(nums[j]!=0){
                swap(nums[j],nums[i]);
                i++;
            }
        }}
};