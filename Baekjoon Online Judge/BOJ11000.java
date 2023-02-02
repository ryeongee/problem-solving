import java.util.*;
import java.io.*;

public class BOJ11000 {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int[][] times = new int[N][2];
        String[] inputArray = new String[2];

        for(int i = 0; i < N; i++){
            inputArray = br.readLine().split(" ");
            times[i][0] = Integer.parseInt(inputArray[0]);
            times[i][1] = Integer.parseInt(inputArray[1]);
        }

        Arrays.sort(times, (o1, o2) -> {
            if(o1[0] == o2[0]){
                return o1[1] - o2[1];
            }
            else return o1[0]- o2[0];
        });
        Queue<Integer> queue = greedy(times);
        System.out.println(queue.size());
    }
    
    public static PriorityQueue<Integer> greedy(int[][] times){
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        
        for(int i = 0; i < N; i++){
            int start = times[i][0];
            int end = times[i][1];
            if(!queue.isEmpty() && queue.peek() <= start){
                queue.poll();
            }
            queue.offer(end);
        }
        return queue;
    }
}
