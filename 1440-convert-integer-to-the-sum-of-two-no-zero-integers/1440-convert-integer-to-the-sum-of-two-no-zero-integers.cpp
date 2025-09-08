class Solution {
public:
    vector<int> getNoZeroIntegers(int n) {
        int a,b;
        for(int i=1;i<n+1;i++){
            a=i,b=n-i;
            if (!brr(a) && !brr(b)){
                return {a,b};
            }   
    }
    return {};
}
    bool brr(int k){
        while(k>0){
            if(k%10==0){
                return true;
            }
            k/=10;
        }
        return false;
    }
};