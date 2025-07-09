import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> dict = new HashMap<>();
        for(int i =0;i<nums.length;i++){
            int dif=target-nums[i];
            if(dict.containsKey(dif)){
                return new int[]{dict.get(dif),i};
            }
            dict.put(nums[i],i);
        }
        return new int[0];
    }
}

