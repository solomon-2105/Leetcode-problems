class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> lastIndex;
        int maxLength = 0, start = 0;

        for (int j = 0; j < s.size(); j++) {
            if (lastIndex.find(s[j]) != lastIndex.end() && lastIndex[s[j]] >= start) {
                start = lastIndex[s[j]] + 1;  // Move start pointer to avoid repeating characters
            }
            lastIndex[s[j]] = j;  // Update last seen index
            maxLength = max(maxLength, j - start + 1);
        }
        return maxLength;
    }
};
