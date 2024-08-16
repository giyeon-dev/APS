class Solution {
    public int solution(int[] array) {
        int answer = 0;
        String nums = "";
        
        for (int num: array) {
            nums += num;
        }
        
        for (int i = 0; i < nums.length(); i++) {
            if (nums.charAt(i) == '7') {
                answer++;
            }
        }
        return answer;
    }
}