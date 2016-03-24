package week_3.change;

import java.util.Scanner;

public class Change {
    private static Scanner scanner;

    private static int getChange(int n) {

        int ans = 0;
        
        if(n >= 10) {
            ans += n/10;
            //System.out.println(n);
            n %= 10;
            //System.out.println(n);
        }
        
        if(n >= 5) {
            ans += n/5;
            //System.out.println(n);
            n %= 5;
            //System.out.println(n);
        }
        
        ans += n;
        
        return ans;
    }

    public static void main(String[] args) {
        scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(getChange(n));
    }
}

