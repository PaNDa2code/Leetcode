public class Solution {
    public int lengthOfLongestSubstring(String s) {
        try {
            if (s.length() <= 1) {
                return s.length();
            }

            int maxLength = 0;
            for (int i = 0; i < s.length(); i++) {
                Set<Character> visited = new HashSet<>();
                int count = 0;
                for (int j = i; j < s.length(); j++) {
                    if (visited.contains(s.charAt(j))) {
                        break;
                    }
                    visited.add(s.charAt(j));
                    count++;
                }
                maxLength = Math.max(maxLength, count);
            }

            return maxLength;
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
            return 0;
        }
    }
}
