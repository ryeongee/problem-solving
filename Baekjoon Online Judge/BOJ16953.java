/**
 * https://www.acmicpc.net/problem/16953
 * 백준 A -> B
 */

import java.util.*;
import java.io.*;

public class BOJ16953 {
    public static long A;
    public static long B;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        A = Long.parseLong(input[0]);
        B = Long.parseLong(input[1]);
        int answer = bfs();
        System.out.println(answer);
    }

    public static int bfs(){
        long a = A, b = B;
        int count = 0;
        Queue<Long> queue = new LinkedList<>();
        queue.add(a);

        while(!queue.isEmpty()){   
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                a = queue.poll();
                if(a == b){
                    return count+1;
                }
                if(a*2 <= b){
                    queue.add(a*2);
                }
                if((a*10)+1 <= b){
                    queue.add(a*10 +1);
                }
            }
            count++;
        }    
        return -1;
    }
}