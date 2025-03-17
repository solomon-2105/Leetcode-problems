class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_map <int,int> um;
        for(int i=0;i<nums.size();i++){
            if(um.find(nums[i])!=um.end()){
                um[nums[i]]+=1;
            }
            else um[nums[i]]=1;
        }
        for(auto it:um){
            if((it.second)%2==1) return false;
        }
        return true;
    }
};