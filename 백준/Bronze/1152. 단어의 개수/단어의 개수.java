import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine().trim();

        int wordCnt = 0;

        if (!input.isEmpty()) {
            wordCnt = 1;

            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) == ' ') {
                    wordCnt++;
                }
            }
        }


        System.out.println(wordCnt);
    }
}
