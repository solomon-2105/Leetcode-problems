import java.util.HashMap;
class Solution {
    public int findLucky(int[] arr) {
        HashMap<Integer,Integer> sinai = new HashMap<>();
        for (int i:arr){
            sinai.put(i,sinai.getOrDefault(i,0)+1);
        }
        int lucky=-1;
        for(var i:sinai.entrySet()){
            if (i.getKey()==i.getValue()){
                lucky=Math.max(lucky,i.getKey());
            }
        }
        return lucky;
    }
}