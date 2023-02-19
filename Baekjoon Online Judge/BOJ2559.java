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

        int[] sumArr = new int[n + 1];
        for(int i = 1; i < n + 1; i++){
            sumArr[i] = sumArr[i - 1] + Integer.parseInt(st.nextToken());
        }

        int maxNum = Integer.MIN_VALUE;
        for(int i = k; i < n + 1; i++){
            int start = i - k + 1;
            int end = i;
            int tmp = prefix(sumArr, start, end);
            if(tmp > maxNum){
                maxNum = tmp;
            }
        }
        System.out.println(maxNum);
    }
    public static int prefix(int[] arr, int start, int end){
        return arr[end] - arr[start - 1];
    }
}
