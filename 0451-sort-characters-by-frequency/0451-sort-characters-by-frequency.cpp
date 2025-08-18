class Solution {
public:
    string frequencySort(string s) {
        vector<int> fr(128,0);
        for(char c:s){
            fr[c]++;
        }
        vector<pair<char,int>>vec;
        for(int i=0;i<128;i++){
            if(fr[i]>0) vec.push_back({(char)i,fr[i]});
        }
        sort(vec.begin(),vec.end(),compare);
        string res="";
        for(auto p:vec){
            res.append(p.second,p.first);
        }
        return res;
    }
    static bool compare(pair<char,int> &a,pair<char,int> &b){
        return a.second>b.second;
    }
};