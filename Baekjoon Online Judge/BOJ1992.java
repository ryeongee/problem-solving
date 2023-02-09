/**
 * https://www.acmicpc.net/problem/1992
 * 백준 1992 쿼드트리
 */

 import java.util.*;
 import java.io.*;

public class BOJ1992 {
    private static int N;
    private static int[][] IMAGE;
    private static String RESULT = "";

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        IMAGE = new int[N][N];
        for (int i = 0; i < N; i++) {
            String[] column = br.readLine().split("");
            for (int j = 0; j < N; j++) {
                IMAGE[i][j] = Integer.parseInt(column[j]);                
            }
        }
        compress(0, 0, N);
        System.out.println(RESULT);
    }
    private static void compress(int startX, int startY, int n){
        if(n == 1){
            RESULT += IMAGE[startX][startY];
        } else {
            boolean flag = true;
            int tmp = IMAGE[startX][startY];
            Loop1:
            for (int i = startX; i < startX + n; i++) {
                for (int j = startY; j < startY + n; j++) {
                    if(tmp != IMAGE[i][j] && n > 1){
                        flag = false;
                        int tmpN = n / 2;
                        RESULT += "(";
                        compress(startX, startY, tmpN);
                        compress(startX, startY + tmpN, tmpN);
                        compress(startX + tmpN, startY, tmpN);
                        compress(startX + tmpN, startY + tmpN, tmpN);
                        RESULT += ")";
                        break Loop1;
                    }
                }
            }
            if(flag){
                RESULT += IMAGE[startX][startY];
            }
        }
    } 
}