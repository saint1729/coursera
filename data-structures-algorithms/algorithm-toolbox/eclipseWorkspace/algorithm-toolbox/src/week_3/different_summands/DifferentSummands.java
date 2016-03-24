package week_3.different_summands;

import java.util.*;

public class DifferentSummands {
    private static Scanner scanner;

    private static List<Integer> optimalSummands(int n) {
        List<Integer> summands = new ArrayList<Integer>();
        
        int i = 1;
        
        while(true) {
            if(n-i <= i) {
                summands.add(n);
                break;
            }
            summands.add(i);
            n -= i;
            i += 1;
        }
        
        return summands;
    }
    
    public static void main(String[] args) {
        scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        List<Integer> summands = optimalSummands(n);
        System.out.println(summands.size());
        for (Integer summand : summands) {
            System.out.print(summand + " ");
        }
    }
}

