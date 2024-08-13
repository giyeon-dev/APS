import java.util.Arrays;
class Solution {
    public int solution(int[] array, int n) {
        int curr = 0;
        int min = 99;
        
        Arrays.sort(array);
        
        for (int i = 0; i < array.length; i++) {
            if (Math.abs(n - array[i]) < min) {
                curr = array[i];
                min = Math.abs(n - array[i]);
                
            } else if (Math.abs(n - array[i]) == min) {
                if (array[i] < curr) {
                    curr = array[i];
                }
            }
        }
        
        return curr;
    }
}