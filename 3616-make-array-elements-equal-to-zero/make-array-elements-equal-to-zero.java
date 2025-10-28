class Solution {
    public int countValidSelections(int[] nums) {
        int n = nums.length;
        int count = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) continue;

            for (int dir : new int[]{-1, 1}) {
                int[] arr = nums.clone(); 
                int curr = i;

                while (curr >= 0 && curr < n) {
                    if (arr[curr] == 0) {
                        curr += dir;
                    } else {
                        arr[curr]--;
                        dir = -dir; 
                        curr += dir;
                    }
                }

                boolean allZero = true;
                for (int val : arr) {
                    if (val != 0) {
                        allZero = false;
                        break;
                    }
                }

                if (allZero) count++;
            }
        }

        return count;
    }
}
