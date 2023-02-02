import java.io.*;
import java.util.*;

public class BOJ14916_오령기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int answer = greedy(n);

        System.out.println(answer);
    }

    public static int myGreedy(int n){
        int answer = 0;
        int state = n;
        int put = 5;
        boolean flag = false;
        if(state < 5){
            flag = true;
        }
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        while(state != 0){
            if(state < 5){
                put = 2;
            }
            if(state == 1 && !flag){
                state += queue.poll();
                if(!queue.isEmpty()){
                    state += queue.poll();
                }
                put = 2;
                flag = true;
            } else if(state == 1 && flag){
                answer = -1;
                break;
            }
            queue.offer(put);
            state -= put;
        }

        if (answer != -1){
            answer = queue.size();
        }
        return answer;
    }

    public static int greedy(int money){
        int coinCount = 0;
        while (money % 5 != 0) {
            money -= 2;
            coinCount++;

            if (money < 0) {
                coinCount = -1;
                break;
            }
        }
        if (coinCount > -1) {
            coinCount += money / 5;
        }
        return coinCount;
    }    
}
