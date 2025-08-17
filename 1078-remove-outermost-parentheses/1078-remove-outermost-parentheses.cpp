class Solution {
public:
    string removeOuterParentheses(string s) {
        string ass="";
        int count=0;
        for(char c:s) {
            if(c=='(') {
                if(count>0) ass.push_back(c);
                count++;
            }else{
                count--;
                if(count>0) ass.push_back(c);
            }
        }
        return ass;
    }
};