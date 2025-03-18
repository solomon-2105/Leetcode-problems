class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int current_sum=0;
        int max_sum=0;
        for(int i:nums){
            if(i==1){ 
                current_sum++;
                max_sum=max(max_sum,current_sum);
            }else{
                current_sum=0;
            }}return max_sum;
    }
};