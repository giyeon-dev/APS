class Solution {
    public String solution(String[] id_pw, String[][] db) {
        for (String[] account : db) {
            String id = account[0];
            String pw = account[1];
            
            if (id_pw[0].equals(id)) {
                if (id_pw[1].equals(pw)) {
                    return "login";
                } else {
                    return "wrong pw";
                }
            }
        }
        return "fail";
    }
}