import java.util.ArrayList; // Import the ArrayList class
import java.util.List;     // Import the List interface

class Solution { // The class to hold our solution
    public List<List<Integer>> permute(int[] nums) { // This is the main function
        List<List<Integer>> result = new ArrayList<>(); // This list will store all the permutations
        backtrack(nums, new ArrayList<>(), new boolean[nums.length], result); // Calls the helper function to do the hard work
        return result; // Returns the list of all permutations
    }

    public void backtrack(int[] nums, List<Integer> current, boolean[] used, List<List<Integer>> result) {
        // This is the core of the algorithm - the recursive "backtracking" function! \U0001f92f
        if (current.size() == nums.length) {
            // Base case: if the current permutation is the same size as the input array,
            // it means we've built a complete permutation.
            result.add(new ArrayList<>(current)); // Add a copy of the current permutation to the result. Important!
            return; // Stop this recursive call
        }

        for (int i = 0; i < nums.length; i++) {
            // Loop through each number in the input 'nums' array
            if (!used[i]) {
                // Check if the number at index 'i' hasn't been used in the current permutation yet.
                used[i] = true; // Mark the number as "used"
                current.add(nums[i]); // Add the number to the current permutation
                backtrack(nums, current, used, result); // Recursively call backtrack to continue building the permutation.
                used[i] = false; // "Unmark" the number (backtrack step):  We're done with this path, so we reset
                current.remove(current.size() - 1); // Remove the last added number (backtrack step):  Go back one step
            }
        }
    }
}