package PythonAlgorithmInterview.Graph.BFS;
/**
 * https://www.acmicpc.net/problem/2606
 * 백준 2606 바이러스
 */

import java.util.*;
import java.io.*;
public class Virus {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int v = 1;
        int[][] adjMatrix = new int[n + 1][n + 1];
        for(int i = 0; i < m; i++){
            String[] column = br.readLine().split(" ");
            int x = Integer.parseInt(column[0]);
            int y = Integer.parseInt(column[1]);
            adjMatrix[x][y] = 1;
            adjMatrix[y][x] = 1;
        }
        MyBFS bfs = new MyBFS(n, v, adjMatrix);
        System.out.print(bfs.getCount());
    }
    
}
class MyBFS {
    private int count = 0;
    MyBFS(int n, int v, int[][] adjMatrix){
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(v);
        visited[v] = true;

        int count = 0;
        while(!queue.isEmpty()){
            v = queue.poll();
            count++;
            for (int i = 1; i < n + 1; i++) {
                if(adjMatrix[v][i] == 1 && !visited[i]){
                    visited[i] = true;
                    queue.add(i);
                }
            }
        }
        this.count = count - 1;
    }

    public int getCount(){
        return this.count;
    }
}