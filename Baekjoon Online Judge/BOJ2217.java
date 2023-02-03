import java.util.*;
import java.io.*;

public class BOJ2217 {
    public static void main(String[] args) throws IOException{
        int answer;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] ropes = new Integer[n];

        for(int i = 0; i < n; i++){
            ropes[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(ropes, Collections.reverseOrder());

        answer = getMaxWeight(ropes, n);
        System.out.println(answer);

    }    
    private static int getMaxWeight(Integer[] ropes, int n){
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        int max = 0;
        for(int i = n; i > 0; i--){
            max = i * ropes[i - 1];
            queue.offer(max);
        }

        return queue.poll();
    }
}
