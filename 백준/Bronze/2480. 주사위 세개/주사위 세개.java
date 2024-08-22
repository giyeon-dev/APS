import java.util.Arrays;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[3];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        int prize;

        if (arr[0] == arr[1] && arr[1] == arr[2]) {
            prize = 10000 + arr[0] * 1000;
        } else if ( arr[0] == arr[1] || arr[0] == arr[2]) {
            prize = 1000 + arr[0] * 100;
        } else if (arr[1] == arr[2]) {
            prize = 1000 + arr[1] * 100;
        } else {
            prize = arr[2] * 100;
        }
        System.out.println(prize);

    }
}