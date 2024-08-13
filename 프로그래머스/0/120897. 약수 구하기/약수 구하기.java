class Solution {
    public int[] solution(int n) {
        
        // 약수 개수 구하기
        int cnt = 0;
        for (int i = 1; i <= n; i++){
            if (n % i == 0) {
                cnt++;
            }
        }
        
        int[] divisor = new int[cnt];
        
        int idx = 0;
        for (int i = 1; i <= n; i++){
            if (n % i == 0) {
                divisor[idx] = i;
                idx++;
            }
        }
        return divisor;
    }
    
}