class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& a, int t) {
        sort(a.begin(), a.end());
        vector<vector<int>> c;
        vector<int> b;
        brr(a, 0, b, t, c);
        return c;
    }
private:
    void brr(vector<int>& a, int i, vector<int>& b, int k, vector<vector<int>>& c) {
        if (i == a.size()) {
            if (k == 0) c.push_back(b);
            return;
        }
        if (a[i] <= k) {
            b.push_back(a[i]);
            brr(a, i + 1, b, k - a[i], c);
            b.pop_back();
        }
        while (i + 1 < a.size() && a[i] == a[i + 1]) i++;
        brr(a, i + 1, b, k, c);
    }
};