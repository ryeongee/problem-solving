import java.util.*;
import java.io.*;

public class BOJ2667 {
    public static int TOTAL_COUNT = 0;
    public static int COUNT = 1;
    public static int N;
    public static int[][] ADJ_MATRIX;
    public static boolean[][] VISITED;
    public static int[] X_MOVE = {-1, 0, 1, 0};
    public static int[] Y_MOVE = {0, -1, 0, 1};

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        List<Integer> answer = new ArrayList<Integer>();
        ADJ_MATRIX = new int[N][N];

        VISITED = new boolean[N][N];
        for (int i = 0; i < N; i++){
            String[] column = br.readLine().split("");
            for (int j = 0; j < N; j++){
                ADJ_MATRIX[i][j] = Integer.parseInt(column[j]);
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if(ADJ_MATRIX[i][j] == 1 && !VISITED[i][j]){
                    TOTAL_COUNT++;
                    COUNT = 1;
                    dfs(i, j);
                    answer.add(COUNT);
                }
            }
        }
        Collections.sort(answer);
        
        System.out.println(TOTAL_COUNT);
        for(int item : answer){
            System.out.println(item);
        }

    }
    
    public static void dfs(int x, int y){
        VISITED[x][y] = true;
        int newX = 0;
        int newY = 0;
        for(int i = 0; i < 4; i++){
            newX = x + X_MOVE[i];
            newY = y + Y_MOVE[i];
            if(newX >= 0 && newY >= 0 && newX < N && newY < N){
                if(ADJ_MATRIX[newX][newY] == 1 && !VISITED[newX][newY]){
                    dfs(newX, newY);
                    COUNT++;
                }
            }
        }
    }
}
