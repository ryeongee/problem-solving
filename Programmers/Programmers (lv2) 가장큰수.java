import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        boolean except = true;
        String[] stringNumbers = new String[numbers.length];
        AsciiComparator asciiComparator = new AsciiComparator();

        for (int i = 0; i < stringNumbers.length; i++) {
            stringNumbers[i] = String.valueOf(numbers[i]);
            if (numbers[i] != 0) except = false;
        }

        Arrays.sort(stringNumbers, asciiComparator);

        for (int i = 0; i < stringNumbers.length; i++)
            answer += stringNumbers[i];
        if (except) answer = "0";
        return answer;
    }
}

class AsciiComparator implements Comparator<String> {
    @Override
    public int compare(String num1, String num2) {
        return (num2 + num1).compareTo(num1 + num2);
    }
}