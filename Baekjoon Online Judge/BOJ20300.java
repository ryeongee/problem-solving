/*
 * https://www.acmicpc.net/problem/20300
 * BOJ 20300
 * 서강근육맨
 */
import java.io.*;
import java.util.*;

public class BOJ20300 {
    private static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        long[] t = new long[N];
        for (int i = 0; i < t.length; i++) {
            t[i] = Long.parseLong(input[i]);
        }
        Arrays.sort(t);
        long maxNum = 0;
        if(N % 2 == 0){
            for (int i = 0; i < N/2; i++) {
                maxNum = Math.max(maxNum, t[i] + t[N-1-i]);
            }
        } else {
            maxNum = t[N - 1];
            for (int i = 0; i < (N-1)/2; i++) {
                maxNum = Math.max(maxNum, t[i] + t[N - 2 - i]);
            }
        }

        System.out.println(maxNum);
        
    }
}
