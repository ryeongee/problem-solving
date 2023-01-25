package PythonAlgorithmInterview.BFS;
/**
 * https://www.acmicpc.net/problem/11725
 * 트리의 부모 찾기
 * DFS
 */
import java.util.*;
import java.io.*;

public class FindParentNode {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] adj = new int[n+1][n+1];
        for(int i = 0; i < n -1; i++){
            String[] column = br.readLine().split(" ");
            int x = Integer.parseInt(column[0]);
            int y = Integer.parseInt(column[1]);
            adj[x][y] = 1;
            adj[y][x] = 1;
        }


    }
}
