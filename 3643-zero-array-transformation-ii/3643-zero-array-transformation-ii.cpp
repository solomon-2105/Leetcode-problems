#include <vector>
using namespace std;

class Solution {
public:
    bool isZeroArray(vector<int>& nums, vector<vector<int>>& queries, int k) {
        vector<int> temp(nums);
        int n = temp.size();
        vector<int> diff(n + 1, 0);

        for (int i = 0; i < k; i++) {
            int l = queries[i][0], r = queries[i][1], val = queries[i][2];
            diff[l] -= val;
            diff[r + 1] += val;
        }

        int curr = 0;
        for (int i = 0; i < n; i++) {
            curr += diff[i];
            temp[i] += curr;
            if (temp[i] > 0) return false;
        }
        return true;
    }

    int minZeroArray(vector<int>& nums, vector<vector<int>>& queries) {
        if (all_of(nums.begin(), nums.end(), [](int x) { return x == 0; })) return 0;  // Handle already zero case

        int low = 1, high = queries.size(), ans = -1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isZeroArray(nums, queries, mid)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};
