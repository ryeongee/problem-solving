/**
 * https://www.acmicpc.net/problem/10986
 * 백준 10986 나머지 합
 */
import java.io.*;
import java.util.*;

public class BOJ10986 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long[] remainArr = new long[n + 1];
        long[] cnt = new long[m];
        st = new StringTokenizer(br.readLine());
        long sum = 0;
        long answer = 0;
        for(int i = 1; i < n + 1; i++){
            sum += Integer.parseInt(st.nextToken());
            remainArr[i] = sum % m;
            if(remainArr[i] == 0){
                answer++;
            }
            cnt[(int) remainArr[i]]++;
        }
        for(int i = 0; i < m; i++){
            if(cnt[i] > 1){
                answer += (cnt[i] * (cnt[i] - 1)) / 2;
            }
        }

        System.out.println(answer);

    }    
}
