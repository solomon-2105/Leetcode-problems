class Solution {
public:
    bool checkPerfectNumber(int num) {
        long long nim=num;
        long long sum=1;
        if(nim<=1){
            return false;}
        for(int i=2;i<sqrt(nim);i++){
            if(nim%i==0){
                sum=sum+i;
                if(i!=nim/i)
                    sum+=nim/i;     
    }}return sum==nim;
}};