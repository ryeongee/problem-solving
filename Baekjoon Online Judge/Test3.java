/**
 * 입력값 〉
[["00011", "01111", "21001", "11001", "01111"], ["00011", "00011", "11111", "12101", "11111"]]
기댓값 〉
[1, 1]
실행 결과 〉
실행한 결괏값 [0,0]이 기댓값 [1,1]과 다릅니다.
〉
[["1111", "1121", "1001", "1111"], ["0000", "0000", "0000", "0002"], ["0000", "0100", "0000", "0002"], ["0000", "0010", "0121", "0010"]]
기댓값 〉
[1, 1, 0, 0]
입력값 〉
[2, 2, -1, 1, 5, -1, 5], [2, 5]
기댓값 〉
[4, 3]
실행 결과 〉
실행한 결괏값 []이 기댓값 [4,3]과 다릅니다.
입력값 〉
[2, 2, -1, 1, 5, -1, 5], [1, 5]
기댓값 〉
[0, 3]
실행 결과 〉
실행한 결괏값 []이 기댓값 [0,3]과 다릅니다.

 */

class Test3 {
    public int solution(String[] bakery_schedule, String current_time, int k) {
        int answer = -1;
        String[] time = current_time.split(":");
        int hour = Integer.parseInt(time[0]);
        int min = Integer.parseInt(time[1]);
        int soldBreads = 0;
        int resultHour = 0;
        int resultMin = 0;
        for(String item : bakery_schedule){
            String[] divideItem = item.split(" ");
            String scehdule = divideItem[0];
            int sellBreads = Integer.parseInt(divideItem[1]);
            String[] outOfOvenTime = scehdule.split(":");
            int tmpHour = Integer.parseInt(outOfOvenTime[0]);
            int tmpMin = Integer.parseInt(outOfOvenTime[1]);
            
            if(tmpHour >= hour && tmpMin >= min){
                resultHour = tmpHour;
                resultMin = tmpMin;

                soldBreads += sellBreads;
                if(soldBreads >= k){
                    break;
                }
            }
        }
        if(soldBreads >= k){
            answer = (resultHour - hour) * 60 + (resultMin - min);

        }
        return answer;
    }
}