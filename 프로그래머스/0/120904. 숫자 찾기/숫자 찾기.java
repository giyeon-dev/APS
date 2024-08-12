class Solution {
    public int solution(int num, int k) {
        
        String n = Integer.toString(num);
        String sk = Integer.toString(k);
        
        int idx = n.indexOf(sk);
        
        if (idx >= 0) {
            return idx + 1;
        } else {
            return -1;
        }
    
    }
}