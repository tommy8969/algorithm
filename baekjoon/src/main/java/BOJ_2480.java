import java.util.Scanner;

public class BOJ_2480 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int fisrtNum = sc.nextInt();
        int secondNum = sc.nextInt();
        int thirdNum = sc.nextInt();
        int prize = 0;

        if(fisrtNum == secondNum && fisrtNum == thirdNum) {
            prize = 10000 + (fisrtNum * 1000);
        } else if(fisrtNum == secondNum || fisrtNum == thirdNum) {
            prize = 1000 + (fisrtNum * 100);
        } else if(secondNum == thirdNum) {
            prize = 1000 + (secondNum * 100);
        } else {
            prize = Math.max(fisrtNum, Math.max(secondNum, thirdNum)) * 100;
        }

        System.out.println(prize);

    }
}
