class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String strk = String.valueOf(k);
        char digit = strk.charAt(0);
        
        StringBuilder sb = new StringBuilder();
        for (int num = i; num <= j; num++){
            sb.append(num);
        }
        
        
        for (int idx = 0; idx < sb.length(); idx++) {
            char c = sb.charAt(idx);
            
            if (c == digit) {
                answer++;
            }
        }
        return answer;
    }
}