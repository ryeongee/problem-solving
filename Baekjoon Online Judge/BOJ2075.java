/**
 * N번째 큰 수 
 * https://www.acmicpc.net/problem/2075 
 */

import java.util.*;
import java.util.stream.Stream;
import java.io.*;

public class BOJ2075 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int answer = 0;
        int n = Integer.parseInt(br.readLine());
        int[] items = new int[n*n];
        inputItemsUsingStringTokenizer(items, n, br);
        
        answer = usingPriorityQueue(items, n);
       
        System.out.println(answer);

        br.close();
    }
    // 방법 1. Java 에서 제공하는 PriorityQueue 사용
    public static int usingPriorityQueue(int[] items, int n){
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((o1, o2) -> Integer.compare(o2, o1));

        for(int item : items){
            maxHeap.add(item);
        }
        
        for(int i = 0; i < n - 1; i++){
            maxHeap.poll();
        }
        int answer = maxHeap.poll(); 
        
        return answer;
    }
    // 방법 2. 우선순위 큐 직접 생성 후 사용
    public static int[] makePriorityQueue(int[] arr, int node){
        for(int i = 1; i < arr.length; i++){
            if(arr[i] > 0){
                arr[i] = node;
            }
        }

        return arr;
    }

    // 입력 방법 1. split() 사용
    static void inputItems(int[] items, int n, BufferedReader br) throws IOException{
        int idx = 0;
        for(int i = 0; i < n; i++){
            String[] colums = br.readLine().split(" ");
            for(int j = 0; j < n; j++){
                items[idx++] = Integer.parseInt(colums[j]);
            }
        }
    }

    // 입력 방법 2. split() + Stream 사용
    static void inputItemsUsingStream(int[] items, int n, BufferedReader br) throws IOException{
        String colums = "";
        for(int i = 0; i < n; i++){
            colums += br.readLine() + " ";
        }
        items = Stream.of(colums.split(" ")).mapToInt(Integer::parseInt).toArray();
    }

    // 입력 방법 3. StringTokenizer 사용
    static void inputItemsUsingStringTokenizer(int[] items, int n, BufferedReader br) throws IOException{
        int idx = 0;
        for(int i = 0; i < n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0; j<n; j++) {
                items[idx++] = Integer.parseInt(st.nextToken());
            }
        }
    }
}
