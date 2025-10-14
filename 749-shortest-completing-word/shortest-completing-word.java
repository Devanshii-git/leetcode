class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        int[] licenseCount = new int[26];

        for (char c : licensePlate.toCharArray()) {
            if (Character.isLetter(c)) {
                licenseCount[Character.toLowerCase(c) - 'a']++;
            }
        }
        
        String result = null;

        for (String word : words) {
            if (isCompleting(word, licenseCount)) {
                if (result == null || word.length() < result.length()) {
                    result = word;
                }
            }
        }
        
        return result;
    }

    private boolean isCompleting(String word, int[] licenseCount) {
        int[] wordCount = new int[26];
        for (char c : word.toCharArray()) {
            wordCount[c - 'a']++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (wordCount[i] < licenseCount[i]) {
                return false;
            }
        }
        return true;
    }
}
