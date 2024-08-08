class Solution {
    public int[] solution(int n) {
        int size = (n + 1) / 2;
        int[] answer = new int[size];
        
        int idx = 0;
        for (int i = 0; i <= n; i ++) {
            if (i % 2 != 0) {
                answer[idx++] = i;
            }
        }
        return answer;
    }
}