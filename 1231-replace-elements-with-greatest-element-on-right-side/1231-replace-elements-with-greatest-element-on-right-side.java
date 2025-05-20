class Solution {
    public int[] replaceElements(int[] arr) {
        int result[] = new int[arr.length];
        result[arr.length-1] = -1;
        int max = -1;

        for(int i=arr.length-2; i>=0; i--){
            max = Math.max(max, arr[i+1]);
            result[i] = max;
        }

        return result;
    }
}