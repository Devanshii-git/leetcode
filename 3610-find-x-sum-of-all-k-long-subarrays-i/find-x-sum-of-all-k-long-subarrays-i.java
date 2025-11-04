import java.util.*;

class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        
        for (int i = 0; i <= n - k; i++) {
            Map<Integer, Integer> freq = new HashMap<>();
            
            for (int j = i; j < i + k; j++) {
                freq.put(nums[j], freq.getOrDefault(nums[j], 0) + 1);
            }
            
            List<int[]> list = new ArrayList<>();
            for (int key : freq.keySet()) {
                list.add(new int[]{key, freq.get(key)});
            }
            list.sort((a, b) -> {
                if (b[1] == a[1]) return b[0] - a[0]; 
                return b[1] - a[1]; 
            });
            
            Set<Integer> topX = new HashSet<>();
            for (int j = 0; j < Math.min(x, list.size()); j++) {
                topX.add(list.get(j)[0]);
            }
            
            int sum = 0;
            for (int j = i; j < i + k; j++) {
                if (topX.contains(nums[j])) {
                    sum += nums[j];
                }
            }
            ans[i] = sum;
        }
        
        return ans;
    }
}
