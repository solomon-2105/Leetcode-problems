#include <bits/stdc++.h>
class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<char> a;
        vector<char> b;
        for(char c:s){
            a.push_back(c);
        }
        for(char d: t){
            b.push_back(d);
        }
        sort(a.begin(),a.end());
        sort(b.begin(),b.end());
        return a==b;
    }
};