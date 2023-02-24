class Solution {
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