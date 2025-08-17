class Solution {
public:
    void reverseRange(string &s, int l, int r) {
        while (l < r) {
            swap(s[l], s[r]);
            l++;
            r--;
        }
    }
    
    string reverseWords(string s) {
        int n = s.size(), i = 0, j = 0;
        while (i < n) {
            while (i < n && s[i] == ' ') i++;
            while (i < n && s[i] != ' ') s[j++] = s[i++];
            while (i < n && s[i] == ' ') i++;
            if (i < n) s[j++] = ' ';
        }
        s.resize(j);
        reverseRange(s, 0, s.size() - 1);
        i = 0;
        while (i < s.size()) {
            int start = i;
            while (i < s.size() && s[i] != ' ') i++;
            reverseRange(s, start, i - 1);
            i++;
        }
        return s;
    }
};
