class Solution {
    public void rotate(int[] nums, int k) {
        int n = nums.length;
        k = k % n; // Handle k > n

        // Recursive reverse function
        reverse(nums, 0, n - 1);
        reverse(nums, 0, k - 1);
        reverse(nums, k, n - 1);
    }

    private void reverse(int[] nums, int l, int h) {
        if (l < h) {
            int temp = nums[l];
            nums[l] = nums[h];
            nums[h] = temp;
            reverse(nums, l + 1, h - 1);
        }
    }
}
