import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [] alphabetCount = new int[26];

        String s = sc.nextLine();

        for (int i = 0; i < s.length(); i++) {
            alphabetCount[s.charAt(i) - 'a']++;
        }

        for (int i = 0; i < alphabetCount.length; i++) {
            System.out.print(alphabetCount[i] + " ");
        }

    }
}