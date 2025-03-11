class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n1 = nums1.size(), n2 = nums2.size();
        vector<int> result(n1 + n2); 
        int i = 0, j = 0, k = 0;

        while (i < n1 && j < n2) {
            if (nums1[i] <= nums2[j]) {
                result[k++] = nums1[i++];
            } else {
                result[k++] = nums2[j++];
            }
        }

        while (i < n1) result[k++] = nums1[i++];
        while (j < n2) result[k++] = nums2[j++];

        int r = result.size();
        if (r % 2 == 0) {
            return (result[r / 2 - 1] + result[r / 2]) / 2.0;
        } else {
            return result[r / 2];
        }
    }
};