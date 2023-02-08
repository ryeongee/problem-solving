/**
 * https://www.acmicpc.net/problem/1992
 * 백준 1992 쿼드트리
 */

 import java.util.*;
 import java.io.*;

public class BOJ1992 {
    private static int N;
    private static int[][] IMAGE;
    private static LinkedList<String> QUAD_TREE;
    private static String quad;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            String column = br.readLine();
            for (int j = 0; j < N; j++) {
                IMAGE[i][j] = column.charAt(j) - '0';                
            }
        }
        QUAD_TREE = new LinkedList<>();
        divideAndConquer(0, 0, N);

    }
    private static void divideAndConquer(int startX, int startY, int n){
        if(n == 1){
            quad += IMAGE[startX][startY];
        } else {
            boolean flag = true;
            int tmp = IMAGE[startX][startY];
            Loop1:
            for (int i = startX; i < startX + n; i++) {
                for (int j = startY; j < startY + n; j++) {
                    if(tmp == IMAGE[i][j] && n > 1){
                        flag = false;
                        int tmpN = n / 2;
                        quad += "(";
                        divideAndConquer(startX, startY, tmpN);
                        divideAndConquer(startX + tmpN, startY, tmpN);
                        divideAndConquer(startX, startY + tmpN, tmpN);
                        divideAndConquer(startX + tmpN, startY + tmpN, tmpN);
                        quad += ")";
                        break Loop1;
                    }
                }
            }
            if(flag){
                quad += IMAGE[startX][startY];
            }
        }
    } 
}