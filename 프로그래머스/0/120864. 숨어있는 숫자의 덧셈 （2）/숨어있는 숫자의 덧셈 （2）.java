class Solution {
    public int solution(String my_string) {
        
        int sum = 0;
        int currNum = 0;
        for (int i = 0; i < my_string.length(); i++){
            char c = my_string.charAt(i);
            
            if (c >= '0' & c <= '9') {
                currNum = currNum * 10 + (c - '0');
            } else {
                sum += currNum;
                currNum = 0;
                }
            }
        sum += currNum;
        return sum;
    }
}