class Test2 {
    public int solution(int n, int m, int k) throws Exception{
        int answer = -1;
        int addLoads = 0;
        while(k > 0){
            addLoads += m - k + 1;
            m = m - k;
            k--;
        }
        if(addLoads > 1000007){
            addLoads %= 1000007;
        }
        if(addLoads < n){
            addLoads = 0;
        }
        return addLoads;
    }
    public static int getResult(int a, int b){
        return a - b + 1;
    }
}