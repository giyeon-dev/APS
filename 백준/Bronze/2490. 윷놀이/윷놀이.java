import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 3; i ++ ) {
            int[] arr = new int[4];
            int cnt = 0;
            for (int j = 0; j < arr.length; j++) {
                arr[j] = sc.nextInt();
                if (arr[j] == 1) {
                    cnt++;
                }
            }

            if (cnt == 4) {
                System.out.println("E");
            } else if (cnt == 3) {
                System.out.println("A");
            } else if (cnt == 2) {
                System.out.println("B");
            } else if (cnt == 1) {
                System.out.println("C");
            } else if (cnt == 0) {
                System.out.println("D");
            }
        }

    }
}