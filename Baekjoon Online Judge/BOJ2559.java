/*
 * https://www.acmicpc.net/problem/2559
 * 백준 2559 수열
 */
import java.util.*;
import java.io.*;

public class BOJ2559 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] arr = new int[n + 1];
        for(int i = 1; i < n + 1; i++){
            arr[i] = arr[i - 1] + Integer.parseInt(st.nextToken());
        }

        int maxNum = 0;
        for(int j = 1; j < n + 1 - k; j++){
            int tmp = prefix(arr, j, j + k);
            if (maxNum > tmp) maxNum = tmp;
        }

        System.out.println(maxNum);
    }
    public static int prefix(int[] arr, int st, int end){
        return arr[end] - arr[st - 1];
    }
}
