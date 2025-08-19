#include <vector>
using namespace std;

class Solution {
public:
    int numberOfAlternatingGroups(vector<int>& colors, int k) {
        int n = colors.size();
        int left = 0, ans = 0, prev = -1;

        for (int right = 0; right < n + k - 1; ++right) {
            int cur_color = colors[right % n];

            if (cur_color == prev) {
                left = right;
            }

            if (right - left + 1 >= k) {
                ans++;
            }

            prev = cur_color;
        }

        return ans;
    }
};
