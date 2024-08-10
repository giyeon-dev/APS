class Solution {
    public int solution(int[] box, int n) {
        int answer = 0;
        int w = box[0] / n;
        int l = box[1] / n;
        int h = box[2] / n;
        
        answer = w * l * h;
        return answer;
    }
}