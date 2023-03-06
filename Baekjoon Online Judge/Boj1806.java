/*
 * https://www.acmicpc.net/problem/1806
 * 백준 부분합
 * 투 포인터
 */
import java.io.*;
import java.util.*;

public class Boj1806{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int s = Integer.valueOf(st.nextToken());
        
        st = new StringTokenizer(br.readLine());
        int[] nums = new int[n + 1];
        for(int i = 0; i < n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
        }
        
        int min = twoPointer(nums, n, s);

        if(min == Integer.MAX_VALUE) System.out.println("0");
        else System.out.println(min);
    }

    public static int twoPointer(int[] arr, int n, int sum){
        int min = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;
        int total = 0;
        while(start <= n && end <= n) {
            if(total >= sum && min > end - start) min = end - start;
            
            if(total < sum) total += arr[end++];
            else total -= arr[start++];
        }
        return min;
    }
}