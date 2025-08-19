class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        long long max_value = 0;
        int max_left = INT_MIN;  // Maximum nums[i] seen so far
        
        for (int j = 1; j < n - 1; j++) {
            max_left = max(max_left, nums[j - 1]);  // Update max nums[i] for i < j
            
            for (int k = j + 1; k < n; k++) {
                long long value = (long long)(max_left - nums[j]) * nums[k];
                max_value = max(max_value, value);
            }
        }
        
        return max_value;
    }
};
