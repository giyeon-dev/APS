class Solution {
    public int solution(String s) {
        int sum = 0;
        String[] arr = s.split(" ");
        
        for (int i = 0; i < arr.length; i++) {
            String num = arr[i];
            if (num.equals("Z")) {
                sum -= Integer.parseInt(arr[i - 1]);
            } else {
                sum += Integer.parseInt(arr[i]);
            }
        }
            
        return sum;
    }
}