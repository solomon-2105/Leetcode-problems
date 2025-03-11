class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> st;
        int i = 0, length = 0, max_length = 0;
        
        for (int j = 0; j < s.size(); j++) {
            while (st.find(s[j]) != st.end()) {
                st.erase(s[i]);
                i++;  
            }
            st.insert(s[j]);
            length = j - i + 1;  
            max_length = max(max_length, length); 
        }
        return max_length;
    }
};