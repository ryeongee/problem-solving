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

    public static int twoPointer(int[] arr, int n, int targetSum){
        int min = Integer.MAX_VALUE;
        int start = 0;
        int end = 0;
        int currentSum = 0;
        while(start <= n && end <= n) {
            if(currentSum >= targetSum && min > end - start){
                min = end - start;
            } else if(currentSum < targetSum){
                currentSum += arr[end++];
            } 
            else {
                currentSum -= arr[start++];
            }
        }
        return min;
    }
}