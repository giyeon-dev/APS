class Solution {
    public String solution(String my_string) {
        StringBuilder answer = new StringBuilder();
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        boolean[] isVowel = new boolean[256];
        
        for (char vowel : vowels) {
            isVowel[vowel] = true;
        }
        
        for (char c: my_string.toCharArray()) {
            if (!isVowel[c]) {
                answer.append(c);
            }
        }
        return answer.toString();
    }
}