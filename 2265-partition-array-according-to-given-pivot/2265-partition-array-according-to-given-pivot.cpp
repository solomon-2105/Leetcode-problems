class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> a;// less than
        vector<int> b;//equal to
        vector<int> c;//greater than
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            if(nums[i]<pivot){
                a.push_back(nums[i]);
            }
            else if(nums[i]==pivot){
                b.push_back(nums[i]);
            }
            else{
                c.push_back(nums[i]);
            }
        }
        for(int i=0;i<a.size();i++){
            res.push_back(a[i]);
        }
        for(int i=0;i<b.size();i++){
            res.push_back(b[i]);
        }
        for(int i=0;i<c.size();i++){
            res.push_back(c[i]);
        }
        return res;
    }
};