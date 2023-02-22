/**
 * https://www.acmicpc.net/problem/11441
 * 백준 11441 합 구하기
 * 결과값 StringBuiler vs array = 724 ms : 1492 ms
 */

import java.util.*;
import java.io.*;

public class BOJ11441{
    public static void main(String[] args) throws IOException{
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] strItems = br.readLine().split(" ");
        int m = Integer.parseInt(br.readLine());

        // int[] prefixSum = new int[m];
        int[] items = makePrefixSum(strItems, n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String[] column = br.readLine().split(" ");
            int[] range = new int[2];
            for (int j = 0; j < 2; j++) {
                range[j] = Integer.parseInt(column[j]);
            }            
            // prefixSum[i] = getPrefixSum(items, range[0], range[1]);
            sb.append(getPrefixSum(items, range[0], range[1]) + "\n");
        }

        // for (int item : prefixSum) {
        //     System.out.println(item);
        // }
        System.out.println(sb.toString());
    }

    public static int[] makePrefixSum(String[] strItems, int n){
        int[] items = new int[n + 1];
        int sum = 0;
        for (int i = 1; i < n + 1; i++) {
            sum += Integer.parseInt(strItems[i - 1]);
            items[i] = sum;
        }
        return items;
    }

    public static int getPrefixSum(int[] items, int start, int end){
        return items[end] - items[start - 1]; 
    }
}