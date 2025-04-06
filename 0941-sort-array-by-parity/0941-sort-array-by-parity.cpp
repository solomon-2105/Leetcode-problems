class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        deque <int> dq;
        for(auto i: nums){
            if(i%2==0) dq.push_front(i);
            else dq.push_back(i);
        }
        nums.clear();
        nums.insert(nums.end(), dq.begin(), dq.end());  
        return nums;
    }
};