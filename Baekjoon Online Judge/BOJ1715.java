/**
 * https://www.acmicpc.net/problem/1715
 * boj 1715
 * 카드정렬하기
 */
import java.io.*;
import java.util.*;

public class BOJ1715 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long answer = 0;
        if(n == 1){

        }
        PriorityQueue<Long> queue = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            queue.offer(Long.parseLong(br.readLine()));
        }
        while(queue.size() > 1){
            long tmp = 0;
            tmp += queue.poll();
            tmp += queue.poll();
            answer += tmp;
            queue.offer(tmp);
        }
        System.out.println(answer);
    }
}
