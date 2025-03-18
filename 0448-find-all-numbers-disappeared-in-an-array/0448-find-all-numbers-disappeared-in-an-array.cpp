class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n=nums.size();
        for(int num:nums) {
            int idx=abs(num)-1;
            if(nums[idx]>0) 
                nums[idx]*=-1;
        }
        vector<int> result;
        for (int i=0;i<n;i++) {
            if(nums[i]>0) 
                result.push_back(i+1);
        }
        return result;
    }
};