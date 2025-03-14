class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        long long l = 0, h = nums.size() - 1;
        merge_sort(nums, l, h);
        return nums;
    }   

private:
    void merge_sort(vector<int>& nums, long long l, long long h) {
        if (l >= h) return;
        
        long long m = l + (h - l) / 2;
        merge_sort(nums, l, m);
        merge_sort(nums, m + 1, h);
        combine(nums, l, m, h);
    }

    void combine(vector<int>& nums, long long l, long long m, long long h) {
        long long lx = m - l + 1, ly = h - m;
        vector<int> x(lx), y(ly);
        
        for (long long i = 0; i < lx; i++) x[i] = nums[l + i];
        for (long long i = 0; i < ly; i++) y[i] = nums[m + 1 + i];

        long long px = 0, py = 0, pa = l;
        
        while (px < lx && py < ly) {
            if (x[px] < y[py]) nums[pa++] = x[px++];
            else nums[pa++] = y[py++];
        }

        while (px < lx) nums[pa++] = x[px++];
        while (py < ly) nums[pa++] = y[py++];
    } 
};
