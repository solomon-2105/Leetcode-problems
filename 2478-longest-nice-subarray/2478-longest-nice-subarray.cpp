#include <vector>
using namespace std;

class Solution {
public:
    int longestNiceSubarray(vector<int>& nums) {
        int maxi = 1, cur = 0, left = 0, right = 0, n = nums.size();

        while (right < n) {
            while ((cur & nums[right]) != 0) { 
                cur ^= nums[left];
                left++;
            }

            cur |= nums[right];
            maxi = max(maxi, right - left + 1);
            right++;
        }
        
        return maxi;
    }
};
