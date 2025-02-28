import java.util.Scanner;
//10810
public class BOJ10810 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();

        int[] basket = new int[N];

        for (int t = 0; t < M; t++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int k = sc.nextInt();

            for (int idx = i - 1; idx < j; idx++) {
                basket[idx] = k;
            }
        }


        for (int num : basket) {
            System.out.print(num + " ");
        }
    }
}

