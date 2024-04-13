import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String words = scanner.nextLine();
        int idx = scanner.nextInt();

        char ans = words.toCharArray()[idx - 1];
        System.out.println(ans);

        scanner.close();
    }

}