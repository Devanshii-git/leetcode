import java.util.*;

class Solution {
    public int[] findErrorNums(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int duplicate = 0;
        int actualSum = 0;
        
        for (int num : nums) {
            if (seen.contains(num)) {
                duplicate = num; 
            }
            seen.add(num);
            actualSum += num;
        }
        
        int n = nums.length;
        int expectedSum = n * (n + 1) / 2;
        int missing = expectedSum - (actualSum - duplicate);
        
        return new int[]{duplicate, missing};
    }
}
