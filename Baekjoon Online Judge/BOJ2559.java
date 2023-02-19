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
        int maxNum = 0;
        for(int i = 1; i < n + 1; i++){
            arr[i] = Integer.parseInt(st.nextToken());
            if(i >= k){
                int sumNum = 0;
                for(int j = 0; j < k; j++){
                    sumNum += arr[i - j];
                }
                if(maxNum < sumNum) maxNum = sumNum;
            }
        }
        System.out.println(maxNum);
    }
}
