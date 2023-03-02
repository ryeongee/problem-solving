import java.io.*;
import java.util.*;

public class Test11441 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] a = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }
        int[] prefixSum = makePrefixSum(a, n);
        int m = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < m; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            
            sb.append(getPrefixSum(start, end, prefixSum) + "\n");
        }
        System.out.println(sb.toString());
    }
    public static int getPrefixSum(int start, int end, int[] prefixSum){
        return prefixSum[end] - prefixSum[start - 1];
    }

    public static int[] makePrefixSum(int[] arr, int n){
        int[] prefixSum = new int[n + 1];
        int sum = 0;
        for(int i = 1; i < n + 1; i++){
            sum += arr[i - 1];
            prefixSum[i] = sum;
        }
        return prefixSum;
    }
}
