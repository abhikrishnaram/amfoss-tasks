import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int m = scanner.nextInt();
        scanner.close();
        int ans = 0;
        if(n%2==0 && n>1)
            ans = n-1;
        System.out.println(ans);
        for(int i = 1; i<m; i++)
            if(i%2!=0&&i!=n)
                System.out.print(i+" ");
        
    }
}