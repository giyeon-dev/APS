class Solution {
    public int[] solution(int[] emergency) {
        int n = emergency.length;
        int[] answer = new int[n];
        
        
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                if (emergency[i] < emergency[j]) {
                    cnt++;
                } 
                
            }
            answer[i] = cnt + 1;
            
        }
        return answer;
    }
}