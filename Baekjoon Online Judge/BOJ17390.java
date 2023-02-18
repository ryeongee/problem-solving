/**
 * https://www.acmicpc.net/problem/17390
 * 백준 17390 이건 꼭 풀어야 해!
 */
import java.util.*;
import java.io.*;
public class BOJ17390{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        Integer[] a = new Integer[n + 1];
        a[0] = 0;
        for(int i = 1; i < n + 1; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }

        int[][] inputs = new int[q][2];
        for(int j = 0; j < q; j++){
            st = new StringTokenizer(br.readLine());
            inputs[j][0] = Integer.parseInt(st.nextToken());
            inputs[j][1] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(a, Collections.reverseOrder());
        int[] b = loadPrefix(a);
        
        for(int k = 0; k < 1; k++){
            System.out.println(getPrefixOfRange(b, inputs[k][0], inputs[k][1]));
        }
    }

    public static int getPrefixOfRange(int[] arr, int start, int end){
        return arr[end] - arr[start - 1];
    }

    public static int[] loadPrefix(Integer[] arr){
        int n = arr.length;
        int[] resultArr = new int[n];
        for (int i = 1; i < n + 1; i++) {
            resultArr[i] += resultArr[i - 1];
        }
        return resultArr;
    }
}
