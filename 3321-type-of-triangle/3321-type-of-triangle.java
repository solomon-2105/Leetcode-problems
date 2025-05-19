class Solution {
    public String triangleType(int[] nums) {
        Arrays.sort(nums);
        Set <Integer> brr= new HashSet<>();
        if (nums[0] + nums[1] <= nums[2]) return "none";
        for (int i: nums){
            brr.add(i);
        }
        if (brr.size()==3) return "scalene";
        else if (brr.size()==2) return "isosceles";
        else return "equilateral";
    }
}