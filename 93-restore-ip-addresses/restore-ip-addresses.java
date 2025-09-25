import java.util.*;

class Solution {
    public List<String> restoreIpAddresses(String s) {
        List<String> result = new ArrayList<>();
        int n = s.length();
        if (n < 4 || n > 12) return result; 

        backtrack(s, 0, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(String s, int idx, List<String> path, List<String> result) {

        if (path.size() == 4) {
            if (idx == s.length()) {
                result.add(String.join(".", path));
            }
            return;
        }


        for (int len = 1; len <= 3 && idx + len <= s.length(); len++) {
            String part = s.substring(idx, idx + len);


            if (part.length() > 1 && part.charAt(0) == '0') break;

      
            int val = Integer.parseInt(part);
            if (val > 255) break;

         
            path.add(part);
            backtrack(s, idx + len, path, result);
            path.remove(path.size() - 1); 
        }
    }
}
