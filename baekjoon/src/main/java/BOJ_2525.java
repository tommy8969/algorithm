import java.util.Scanner;

public class BOJ_2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int H = sc.nextInt();
        int M = sc.nextInt();
        int cookTime = sc.nextInt();

        int endTime = 0;

        if (M + cookTime >= 60) {
           endTime = (M + cookTime) % 60;
           H = H + ((M + cookTime) / 60);
        } else {
            endTime = M + cookTime;
        }

        if (H >= 24) {
            H -= 24;
        }

        System.out.println(H + " " + endTime);

    }
}
