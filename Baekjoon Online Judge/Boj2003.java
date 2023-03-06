/*
 * https://www.acmicpc.net/problem/2003
 * 백준 2003 수들의 합 2
 * 투 포인터
 */
import java.util.*;
import java.io.*;

public class Boj2003{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] a = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println(twoPointer2(a, m));
    }
    public static int twoPointer(int[] arr, int target){
        int start = 0;
        int end = 0;
        int sum = 0;
        int count = 0;
        while(end < arr.length){
            if(sum == target){
                count++;
            } 
            if(sum < target){
                sum += arr[end];
                end++;
            } else{
                sum -= arr[start];
                start++;
            }
        }
        return count;
    }
    static int twoPointer2(int[] arr, int m) {
		int count = 0;
		int startPoint = 0, endPoint = 0;
		int len = arr.length;
		int sum = 0;
		
		while(true) {
			if(sum >= m) {  
				sum -= arr[startPoint++];
				
			}
			else if(endPoint >= len) {
				break;
			}
			else { 
				sum += arr[endPoint++];
			}
			
			if(sum == m) {
				count++;
			}
		}
		
		return count;
	}
}