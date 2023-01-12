class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        Arrays.sort(citations);
        for (int i = 0; i < citations.length; i++) {
            int hIndex = citations.length - i;
            if (citations[i] >= hIndex) return hIndex;
        }
        return answer;
    }
}