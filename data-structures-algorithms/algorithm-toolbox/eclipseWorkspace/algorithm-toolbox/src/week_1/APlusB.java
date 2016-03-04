package week_1;
import java.util.Scanner;

class APlusB {
    private static Scanner s;

	public static void main(String[] args) {
        s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        System.out.println(a + b);
    }
}