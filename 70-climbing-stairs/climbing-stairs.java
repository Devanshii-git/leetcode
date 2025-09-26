class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1; 
        if (n == 2) return 2;
        
        int first = 1; 
        int second = 2; 
        int totalWays = 0;
        
        for (int i = 3; i <= n; i++) {
            totalWays = first + second; 
            first = second;
            second = totalWays;
        }
        
        return totalWays;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.climbStairs(2)); 
        System.out.println(sol.climbStairs(3)); 
    }
}
