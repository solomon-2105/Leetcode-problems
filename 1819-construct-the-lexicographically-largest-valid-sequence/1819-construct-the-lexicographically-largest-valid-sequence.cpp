#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        vector<int> result(2 * n - 1, 0); // Initialize with 0s
        vector<bool> used(n + 1, false);  // To track placed numbers
        backtrack(result, used, 0, n);
        return result;
    }

private:
    bool backtrack(vector<int>& result, vector<bool>& used, int index, int n) {
        if (index == result.size()) return true; // Successfully filled
        
        if (result[index] != 0) return backtrack(result, used, index + 1, n); // Skip filled
        
        for (int num = n; num >= 1; --num) { // Try from largest to smallest
            if (used[num]) continue;  // Skip used numbers
            if (num == 1) { // Place '1' (only one occurrence)
                result[index] = 1;
                used[1] = true;
                if (backtrack(result, used, index + 1, n)) return true;
                result[index] = 0;
                used[1] = false;
            } else { // Place larger numbers (2 to n)
                int nextIndex = index + num;
                if (nextIndex < result.size() && result[nextIndex] == 0) {
                    result[index] = result[nextIndex] = num;
                    used[num] = true;
                    if (backtrack(result, used, index + 1, n)) return true;
                    result[index] = result[nextIndex] = 0;
                    used[num] = false;
                }
            }
        }
        return false; // No valid placement found
    }
};
