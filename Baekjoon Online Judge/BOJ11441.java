/**
 * https://www.acmicpc.net/problem/11441
 * 백준 11441 합 구하기
5
10 20 30 40 50
5
1 3
2 4
3 5
1 5
4 4
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

        int[] prefixSum = new int[n];
        int[] items = makePrefixSum(strItems, n);
        for (int i = 0; i < m; i++) {
            String[] column = br.readLine().split(" ");
            int[] range = new int[2];
            for (int j = 0; j < 2; j++) {
                range[j] = Integer.parseInt(column[j]);
            }
            System.out.println("st : "+ range[0] + " end : "+range[1]);
            prefixSum[i] = getPrefixSum(items, range[0], range[1]);
        }

        for (int item : prefixSum) {
            System.out.println(item);
        }
    }

    public static int[] makePrefixSum(String[] strItems, int n){
        int[] items = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += Integer.parseInt(strItems[i]);
            items[i] = sum;
        }
        return items;
    }

    public static int getPrefixSum(int[] items, int start, int end){
        if(start == 1){
            return items[end - 1];
        } else{
            return items[end - 1] - items[start - 2]; 
        }
    }
}