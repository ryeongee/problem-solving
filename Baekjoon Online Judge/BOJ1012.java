/**
 * https://www.acmicpc.net/problem/1012
 * 백준 1012
 * 유기농 배추
 * DFS
 */
import java.util.*;
import java.io.*;

public class BOJ1012 {
    private static int T;
    private static int M, N, K;
    private static int X, Y;
    private static int[] MOVE_X = {0, 0, -1, 1};
    private static int[] MOVE_Y = {1, -1, 0, 0};
    private static boolean[][] VISITED;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = new String[3];
        int[] inputNum = new int[3];
        List<Integer> answerList = new ArrayList<>();
        T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            int bugCount = 0;
            input = br.readLine().split(" ");
            for (int j = 0; j < input.length; j++) {
                inputNum[j] = Integer.parseInt(input[j]);
            }
            M = inputNum[0];
            N = inputNum[1];
            K = inputNum[2];
            int[][] land = new int[M][N];
            VISITED = new boolean[M][N];

            for (int j = 0; j < K; j++) {
                String[] posString = br.readLine().split(" ");
                int x = Integer.parseInt(posString[0]);
                int y = Integer.parseInt(posString[1]);
                land[x][y] = 1;
            }

            for (int j = 0; j < M; j++) {
                for (int j2 = 0; j2 < N; j2++) {
                    if(!VISITED[j][j2] && land[j][j2] == 1){
                        VISITED[j][j2] = true;
                        dfs(land, j, j2);
                        bugCount++;
                    }
                }
            }
            answerList.add(bugCount);
        }
        for (Integer answer : answerList) {
            System.out.println(answer);
        }
    }
    public static void dfs(int[][] land, int x, int y){
        for (int i = 0; i < 4; i++) {
            int newX = x + MOVE_X[i];
            int newY = y + MOVE_Y[i];

            if(newX >= 0 && newX < M && newY >= 0 && newY < N){
                if(!VISITED[newX][newY] && land[newX][newY] == 1){
                    VISITED[newX][newY] = true;
                    dfs(land, newX, newY);
                }
            }
        }
    }    
}
