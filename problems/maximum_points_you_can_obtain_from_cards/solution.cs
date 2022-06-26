public class Solution {
    public int MaxScore(int[] cardPoints, int k) {
        int len = cardPoints.Length;
        if(len == 0 || k == 0)
            return 0;
        
        int sum = 0;
        int tempSum = 0;
        for(int i=0; i<k; i++)
        {
            sum += cardPoints[i];
        }
        
        int counter = k-1;
        int endCounter = len - 1;
        tempSum = sum;
        while(counter >= 0)
        {
            tempSum -= cardPoints[counter--];
            tempSum += cardPoints[endCounter--];
            if(tempSum > sum)
            {
                sum = tempSum;
            }
        }
        
        return sum;
    }
}