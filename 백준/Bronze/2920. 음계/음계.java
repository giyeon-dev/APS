import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [] order = new int[8];
        for (int i = 0; i < order.length; i++) {
            order[i] = sc.nextInt();
        }

        boolean ascending = true;
        boolean descending = true;
        for (int i = 0 ; i < order.length - 1; i ++) {
            if (order[i + 1] >  order[i]) {
                descending = false;
            } else if (order[i + 1] < order[i]) {
               ascending = false;
            }
        }

        if (ascending) {
            System.out.println("ascending");
        } else if (descending) {
            System.out.println("descending");
        } else {
            System.out.println("mixed");
        }

    }
}