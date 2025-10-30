import java.util.*;

class Solution {
    public boolean hasGroupsSizeX(int[] deck) {
        if (deck.length < 2) return false;

        Map<Integer, Integer> countMap = new HashMap<>();
        for (int card : deck) {
            countMap.put(card, countMap.getOrDefault(card, 0) + 1);
        }

        int gcd = 0;
        for (int count : countMap.values()) {
            gcd = getGCD(gcd, count);
        }

        return gcd >= 2;
    }

    private int getGCD(int a, int b) {
        if (b == 0) return a;
        return getGCD(b, a % b);
    }
}
