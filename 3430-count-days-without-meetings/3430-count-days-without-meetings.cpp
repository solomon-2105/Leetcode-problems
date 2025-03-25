#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countDays(int days, vector<vector<int>>& meetings) {
        sort(meetings.begin(), meetings.end());
        int freeDays = 0, prev_end = 0;
        for (auto& meeting : meetings) {
            int start = meeting[0], end = meeting[1];
            if (start > prev_end + 1) {
                freeDays += (start - prev_end - 1);
            }
            prev_end = max(prev_end, end);
        }
        if (prev_end < days) {
            freeDays += (days - prev_end);
        }

        return freeDays;
    }
};
