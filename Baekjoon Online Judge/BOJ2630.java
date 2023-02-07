/**
 * https://www.acmicpc.net/problem/2630
 * 백준 2630 색종이 만들기
 */
import java.io.*;
import java.util.*;

public class BOJ2630 {
    private static int N;
    private static int PAPER[][];
    private static int WHITE_COUNT;
    private static int BLUE_COUNT;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        PAPER = new int[N][N];
        for(int i = 0; i < N; i++){
            String[] column = br.readLine().split(" ");
            for(int j = 0; j < N; j++){
                PAPER[i][j] = Integer.parseInt(column[j]);
            }
        }
        WHITE_COUNT = 0;
        BLUE_COUNT = 0;
        divideAndConquer(0,0, N);
        System.out.println(WHITE_COUNT);
        System.out.println(BLUE_COUNT);
    }
    private static void divideAndConquer(int startX, int startY, int n){
        if(n == 1){
            if(PAPER[startX][startY] == 1){
                BLUE_COUNT++;
            } else{
                WHITE_COUNT++;
            }
        } else{
            boolean white_flag = false;
            boolean blue_flag = false;
            boolean flag = true;
            int tmp;
            if(PAPER[startX][startY] == 0){
                white_flag = true;
                tmp = 0;
            } else{
                blue_flag = true;
                tmp = 1;
            }
            Loop1:
            for (int i = startX; i < startX + n; i++) {
                for (int j = startY; j < startY + n; j++) {
                    if(PAPER[i][j] != tmp && n > 1){
                        int tmpN = n / 2;
                        divideAndConquer(startX, startY, tmpN);
                        divideAndConquer(startX, startY + tmpN, tmpN);
                        divideAndConquer(startX + tmpN, startY, tmpN);
                        divideAndConquer(startX + tmpN, startY + tmpN, tmpN);
                        flag = false;
                        break Loop1;
                    }
                }
            }
            if(blue_flag && flag){
                BLUE_COUNT++;
            }
            if(white_flag && flag){
                WHITE_COUNT++;
            }
        }
    }
}
