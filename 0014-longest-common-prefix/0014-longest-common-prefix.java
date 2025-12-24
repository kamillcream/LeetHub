class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) return "";

        Arrays.sort(strs);
        String first = strs[0];
        String last = strs[strs.length - 1];

        int idx = 0;

        while(idx < first.length() && idx < last.length() && first.charAt(idx) == last.charAt(idx)) {
            idx++;
        }

        return first.substring(0, idx);
    }
}