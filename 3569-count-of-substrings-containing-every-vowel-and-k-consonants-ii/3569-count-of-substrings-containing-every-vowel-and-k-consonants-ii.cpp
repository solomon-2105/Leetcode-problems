class Solution {
public:
    long long countOfSubstrings(string word, int k) {
        long long n = word.size();
        vector<long long> nextcons(n, n);
        long long cur = n;
    
    for (long long i = n - 1; i >= 0; --i) {
        nextcons[i] = cur;
        if (string("aeiou").find(word[i]) == string::npos) {
            cur = i;
        }
    }
    
    long long left = 0, right = 0, cons = 0, ans = 0;
    unordered_map<char, long long> d;
    
    while (right < n) {
        if (string("aeiou").find(word[right]) != string::npos) {
            d[word[right]]++;
        } else {
            cons++;
        }
        
        while (left < n && cons > k) {
            if (string("aeiou").find(word[left]) != string::npos) {
                if (--d[word[left]] == 0) {
                    d.erase(word[left]);
                }
            } else {
                cons--;
            }
            left++;
        }
        
        while (left < n && cons == k && d.size() == 5) { // Valid window
            long long nextc = nextcons[right];
            ans += (nextc - right);
            if (string("aeiou").find(word[left]) != string::npos) {
                if (--d[word[left]] == 0) {
                    d.erase(word[left]);
                }
            } else {
                cons--;
            }
            left++;
        }
        right++;
    }
    
    return ans;
}
    };