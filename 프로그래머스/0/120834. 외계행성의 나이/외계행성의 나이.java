class Solution {
    public String solution(int age) {
        String answer = "";
        String n = Integer.toString(age);
        
        for (int i = 0; i < n.length(); i++){
            char c = n.charAt(i);
            char changeChar = (char) (c - '0' + 'a');
            
            answer += changeChar;
        }
        return answer;
    }
}