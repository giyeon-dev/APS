class Solution {
    public int[] solution(int money) {
        
        int cnt = money / 5500;
        int remain = money % 5500;
        
        int[] answer = {cnt, remain};
        
        return answer;
    }
}