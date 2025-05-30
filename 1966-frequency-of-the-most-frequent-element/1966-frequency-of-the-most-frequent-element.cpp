class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end()); // Sort the array → O(N log N)
        long long l = 0, total = 0, maxFreq = 0;

        for (long long r = 0; r < nums.size(); r++) {
            total += nums[r];  // Expand the window

            // Instead of recalculating everything, only adjust total when necessary
            if ((r - l + 1) * nums[r] - total > k) {
                total -= nums[l]; // Remove smallest element in the window
                l++; // Shrink the window
            }

            maxFreq = max(maxFreq, r - l + 1);
        }
        return maxFreq;
    }
};
