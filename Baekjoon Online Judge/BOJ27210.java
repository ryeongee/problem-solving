/**
 * https://www.acmicpc.net/problem/27210
 * 백준 27210 신을 모시는 사당
 */
import java.io.*;
import java.util.*;

public class BOJ27210 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int[] prefix = new int[n + 1];
        for (int i = 1; i < n + 1; i++) {
            int ipt = Integer.parseInt(st.nextToken());
            if(ipt == 1){
                prefix[i] = prefix[i - 1] + 1;
            } else {
                prefix[i] = prefix[i - 1] - 1;
            }
        }
        Arrays.sort(prefix);
        int answer = prefix[n] - prefix[0];
        System.out.println(Math.abs(answer));
    }    
}
