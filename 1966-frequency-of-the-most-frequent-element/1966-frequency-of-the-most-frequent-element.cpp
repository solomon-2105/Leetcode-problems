class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    long long l = 0, total = 0, maxFreq = 0; 
    for (long long r = 0; r < nums.size(); r++) {
        total += nums[r]; 
        while ((r - l + 1) * nums[r] - total > k) {  
            total -= nums[l];             l++;  
        }
        maxFreq = max(maxFreq, r - l + 1);
    }
    return maxFreq;
}
};