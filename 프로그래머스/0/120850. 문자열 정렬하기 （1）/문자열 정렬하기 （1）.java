import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        
        int cnt = 0;
        for (int i = 0; i < my_string.length(); i++){
            char c = my_string.charAt(i);
            if (c >= '0' && c <= '9') {
                cnt++;
            }
        }
        
        int[] numArray = new int[cnt];
        int idx = 0;
        for (int i = 0; i < my_string.length(); i++) {
            char c = my_string.charAt(i);
            if (c >= '0' && c <= '9') {
                numArray[idx++] = c - '0';
            }
        }
        Arrays.sort(numArray);
        
        return numArray;
    }
}