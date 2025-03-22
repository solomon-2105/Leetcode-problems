class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end()); // Step 1: Sort the array
        int n = nums.size();
        vector<long long> prefix(n + 1, 0); // Prefix sum array
        
        // Step 2: Compute prefix sum
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + nums[i - 1];
        }

        int left = 1, right = n, result = 1;

        // Step 3: Binary Search on window size
        while (left <= right) {
            int mid = (left + right) / 2;
            bool possible = false;

            // Check if we can form a window of size `mid`
            for (int r = mid - 1; r < n; r++) {
                int l = r - mid + 1;
                long long sum = prefix[r + 1] - prefix[l];
                long long required = (long long)nums[r] * mid - sum;
                
                if (required <= k) {
                    possible = true;
                    break;
                }
            }

            if (possible) {
                result = mid; // Increase window size
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
};
