import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        Arrays.sort(array);
        
        for (int i = 0; i < array.length; i ++){
            if (i == array.length / 2) {
                answer = array[i];
            }
        }
        
        return answer;
    }
}