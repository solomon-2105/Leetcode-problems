class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int,int> sinai;
        for(int i=0;i<nums.size();i++){
            int comp=target-nums[i];
            if (sinai.find(comp)!=sinai.end()){
                return {sinai[comp],i};
            }
            sinai[nums[i]]=i;

            }
    
    return {};
    }};