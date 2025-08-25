class Solution {
    public boolean partitionArray(int[] nums, int k) {
        if (nums.length%k!=0) {
            return false;
        } else {
            int bitch=nums.length/k;
            java.util.HashMap<Integer,Integer> a=new java.util.HashMap<>();
            for (int i:nums) {
                a.put(i,a.getOrDefault(i,0)+1);
            }
            for (int w:a.values()) {
                if (w>bitch) return false;
            }
            return true;
        }
    }
}
