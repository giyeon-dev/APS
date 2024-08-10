class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i = 0; i < my_string.length(); i++) {
            char s = my_string.charAt(i);
            if (Character.isUpperCase(s)) {
                answer += Character.toLowerCase(s);
            } else {
                answer += Character.toUpperCase(s);
            }
        }
        return answer;
    }
}