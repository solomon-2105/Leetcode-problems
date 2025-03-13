class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) swap(nums1, nums2);
        unordered_set<int> s(nums1.begin(), nums1.end());
        vector<int> result;
        for (int num : nums2) {
            if (s.erase(num)) { 
                result.push_back(num);
            }
        }    
        return result;
    }
};