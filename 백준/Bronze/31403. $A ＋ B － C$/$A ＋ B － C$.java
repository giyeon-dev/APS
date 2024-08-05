import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int ans1 = A + B - C;
        System.out.println(ans1);

        String strA = Integer.toString(A);
        String strB = Integer.toString(B);

        String strAB = strA + strB;

        int numAB = Integer.parseInt(strAB);

        int ans2 = numAB - C;

        System.out.println(ans2);

    }
}