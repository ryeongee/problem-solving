class Solution {
    public static int[] MOVE_X = {0, 0, 1, -1};
    public static int[] MOVE_Y = {1, -1, 0, 0};
    public static int[][] MAP;
    public static boolean[][] VISITED;
    public static int N;
    public int[] solution(String[][] boards) {
        int[] answer = {};
        int totalCount = 0;
        answer = new int[boards.length];
        
        for(String[] board : boards){
            N = board.length;
            MAP = new int[N][N];
            VISITED = new boolean[N][N];
            int[] position = new int[2];
            int count = 0;
            for(int i = 0; i < N; i++){
                String[] column = board[i].split("");
                for(int j = 0; j < N; j++){
                    MAP[i][j] = Integer.parseInt(column[j]);
                    if(MAP[i][j] == 2){
                        position[0] = i;
                        position[1] = j;
                        count++;
                    } else if(MAP[i][j] == 1){
                        count++;
                    } 
                }
            }
            VISITED[position[0]][position[1]] = true;
            dfs(position[0], position[1]);
            
            int tmpCount = 0;
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    if(VISITED[i][j]){
                        tmpCount++;
                    }
                }
            }

            if(count == tmpCount){
                answer[totalCount] = 1;
            } else {
                answer[totalCount] = 0;
            }

            totalCount++;
        }

        return answer;
    }
    public static void dfs(int x, int y){
        for(int i = 0; i < 4; i++){
            x += MOVE_X[i];
            y += MOVE_Y[i];
            if(x >= 0 && x < N && y >= 0 && y < N){
                if(!VISITED[x][y] && MAP[x][y] == 1){
                    VISITED[x][y] = true;
                    dfs(x, y);
                }
            }
        }
    }
}