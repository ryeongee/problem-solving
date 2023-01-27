    package PythonAlgorithmInterview.Graph.BFS;

    import java.util.*;
    import java.util.stream.Stream;
    import java.io.*;

    public class DFSBFSTest {
        public static void main(String[] args) throws IOException{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            int[] inputArr1 = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
            int n = inputArr1[0];
            int m = inputArr1[1];
            int v = inputArr1[2];

            int[][] adjacencyMatrix = new int[n + 1][n + 1];
            
            for (int i = 0; i < m; i++) {
                int[] inputArr = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
                adjacencyMatrix[inputArr[0]][inputArr[1]] = 1;
                adjacencyMatrix[inputArr[1]][inputArr[0]] = 1;
            }
            DFS dfs = new DFS(n, v, adjacencyMatrix);
            System.out.println();
            BFS bfs = new BFS(n, v, adjacencyMatrix);
        }

    }
    /**
     * BFS - 인접행렬을 이용한 방식으로 구현
     * 구현이 빠르다. 
     * 탐색 시 인접 리스트 방식에 비해 빠르다.  
     * 탐색 시간복잡도 : 인접 리스트 = O(v) 인접 행렬 = O(1)
     */
    class BFS {
        public BFS(int n, int v, int[][] adjacencyMatrix) {
            boolean[] visited = new boolean[n + 1];
            int[][] adjMatrix = adjacencyMatrix;

            Queue<Integer> queue = new LinkedList<>();
            queue.add(v);
            visited[v] = true;

            while(!queue.isEmpty()){
                v = queue.poll();
                System.out.print(v + " ");
                for (int i = 1; i <= n; i++) {
                    if (adjMatrix[v][i] == 1 && !visited[i]) {
                        queue.add(i);
                        visited[i] = true;
                    }
                }
            }
        }

    }

    class DFS {
        public DFS(int n, int v, int[][] adjMatrix){
            boolean[] visited = new boolean[n+1];
            dfs(n, v, visited, adjMatrix);
        }

        static void dfs(int n, int v, boolean[] visited, int[][] adjMatrix){
            visited[v] = true;
            System.out.print(v + " ");

            for(int i = 1; i < n + 1; i++) {
                if(adjMatrix[v][i] == 1 && !visited[i]) {
                    dfs(n, i, visited, adjMatrix);
                }
            }
        }
    }
