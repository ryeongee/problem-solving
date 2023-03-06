/*
 * https://www.acmicpc.net/problem/20922
 * 백준 겹치는건 싫어
 * 투 포인터
 */
import java.io.*;
import java.util.*;

public class Boj20922{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken()), k = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = Integer.valueOf(st.nextToken());
        }
        
        System.out.println(twoPointer(a, n, k));
    }
    public static int twoPointer(int[] arr, int n, int maxDuplicate){
        int maxLength = Integer.MIN_VALUE;
        int[] duplicateCountArray = new int[100001];
        int start = 0, end = 0;
        while(start <= end){
            if(end <= n - 1 && duplicateCountArray[arr[end]] < maxDuplicate){
                duplicateCountArray[arr[end]]++;
                end++;
            } else if(duplicateCountArray[arr[end]] == maxDuplicate){
                duplicateCountArray[arr[start]]--;
                start++;
            }
            maxLength = Math.max(maxLength, end - start);
            if(end == n){
                break;
            }
        }
        return maxLength;
    }
}