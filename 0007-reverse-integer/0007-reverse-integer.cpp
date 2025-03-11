class Solution {
public:
    int reverse(int x) {
        int r; 
        long sum=0;
        while(x!=0){
            r=x%10;
            sum=sum*10+r;
            x=x/10;
        }
        if (sum < -2147483648 || sum > 2147483647) {
            return 0;
        }
        return (int)sum;
    }
};