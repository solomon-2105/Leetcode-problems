class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        int n= grid.size() * grid.size();
        int rep=-1,mis=-1;
        unordered_map <int,int> u;
        for(auto &i:grid){
            for(int j:i){
                u[j]+=1;
            }
        }
        for(int i=1;i<=n;i++){
            if(u[i]==2) rep=i;
            if(u[i]==0) mis=i; 
        }
    return {rep,mis};
    }
};