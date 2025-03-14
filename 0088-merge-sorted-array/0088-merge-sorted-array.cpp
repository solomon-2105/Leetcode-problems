class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i=0,j=0,p=0;
        vector <int> v(m+n);
        while(i<m && j<n){
            if(nums1[i]<=nums2[j]){
                v[p++]=nums1[i++];
            }
            else{
                v[p++]=nums2[j++];
            }
        }
        while(i<m) v[p++]=nums1[i++];  
        while(j<n) v[p++]=nums2[j++];
    
        nums1=v;
    }
};