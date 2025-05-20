class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] diff = new int[n + 1]; // diff array for prefix sum trick

        // Step 1: mark the ranges
        for (int[] query : queries) {
            int left = query[0];
            int right = query[1];
            diff[left] += 1;
            if (right + 1 < n) {
                diff[right + 1] -= 1;
            }
        }

        // Step 2: compute prefix sum to get count of operations per index
        int[] opCount = new int[n];
        opCount[0] = diff[0];
        for (int i = 1; i < n; i++) {
            opCount[i] = opCount[i - 1] + diff[i];
        }

        // Step 3: check if each number can be made zero
        for (int i = 0; i < n; i++) {
            if (nums[i] > opCount[i]) return false;
        }

        return true;
    }
}
