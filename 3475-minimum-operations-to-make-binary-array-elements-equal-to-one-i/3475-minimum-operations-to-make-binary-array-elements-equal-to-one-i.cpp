class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        vector<int> flipRecord(n, 0); 
        int flips = 0, flipCount = 0;
        for (int i = 0; i < n; i++) {
            if (i >= 3) {
                flipCount -= flipRecord[i - 3];
            }
            if ((nums[i] + flipCount) % 2 == 0) {
                if (i > n - 3) {
                    return -1; 
                }
                flips++;
                flipCount++;
                flipRecord[i] = 1;
            }
        }
        return flips;
}
};