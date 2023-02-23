import java.util.*;
import java.io.*;

public class Main {
    public static int[] MOVE_X = {1, 0, 0, -1};
    public static int[] MOVE_Y = {0, 1, -1, 0};
    public static boolean[][] VISITED;
    public static int[][] LAND;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < t; i++){
            int count = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());            
            int k = Integer.parseInt(st.nextToken());
            VISITED = new boolean[m][n];
            LAND = new int[m][n]; 
            for(int j = 0; j < k; j++){
                st = new StringTokenizer(br.readLine());
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                LAND[x][y] = 1;
            }

            for(int x = 0; x < m; x++){
                for (int y = 0; y < n; y++){
                    if(LAND[x][y] == 1 && !VISITED[x][y]){
                        VISITED[x][y] = true;
                        dfs(x, y);
                        count++;
                    }
                }
            }
            sb.append(count + "\n");
        }
        System.out.print(sb.toString());
    }
    public static void dfs(int x, int y){
        for(int i = 0; i < 4; i++){
            int newX = x + MOVE_X[i];
            int newY = y + MOVE_Y[i];

            if(newX >= 0 && newX < LAND.length && newY >= 0 && newY < LAND[0].length){
                if(LAND[newX][newY] == 1 && !VISITED[newX][newY]){
                    VISITED[newX][newY] = true;
                    dfs(newX, newY);
                }
            }
        }
    }
}
