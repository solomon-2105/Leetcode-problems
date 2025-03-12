class Solution {
public:
    bool isPalindrome(string s) {
        string res="";
        for(char si:s){
            if(isalnum(si)){
                res+=tolower(si);
            }
        }
        int n=res.size();
        return checkPalindrome(0,res,n);
    }

    bool checkPalindrome(int i,string &res , int n){
        if(i>=n/2) return true;
        if(res[i]!=res[n-i-1]) return false;
        return checkPalindrome(i+1, res, n);
    }
};