import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        int min = 999999;
        for (int i = 0; i < 7; i++) {
            int n = sc.nextInt();
            if (n % 2 != 0) {
                sum += n;
                if (n < min) {
                    min = n;
                }
            }

        }
        if (sum == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sum);
            System.out.println(min);
        }
    }
}