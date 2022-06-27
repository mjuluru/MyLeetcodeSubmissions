public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int len = nums.Length;
        if(len == 0)
            return 0;
        
        int i=0;
        while(i < len)
        {
            if(nums[i] == val)
            {
                nums[i] = -1;
            }
            
            i++;
        }
        
        i = 0;
        int negCounter = 0;
        
        while(negCounter < len)
        {
            if(nums[negCounter] == -1)
            {
                negCounter++;
                continue;
            }
            
            int temp = nums[i];
            nums[i] = nums[negCounter];
            nums[negCounter] = temp;
            i++;
            negCounter++;
        }
        
        int j=0;
        while(j < len)
        {
            if(nums[j] > -1)
            {
                j++;
            }
            else
            {
                break;
            }
        }
        
        return j;
    }
}