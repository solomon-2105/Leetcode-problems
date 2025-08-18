class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> u={{'I',1},{'V',5},{'X',10},{'L',50},{'C',100},{'D',500},{'M',1000}};
        int count=0;
        for(int i=0;i<s.size();i++){
            if(((i+1)<s.size()) && (u[s[i]]<u[s[i+1]])){
                count-=u[s[i]];
            }
            else{
                count+=u[s[i]];
            }
        }
        return count;
    }
};