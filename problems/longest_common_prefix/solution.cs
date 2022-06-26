public class Solution {
    public string LongestCommonPrefix(string[] strs) {
        int len = strs.Length;
        if(len == 0 )
        {
            return "";
        }
        
        if(len == 1 )
        {
            return strs[0];
        }
        
        string cmn = strs[0];
        int i=1;
        while(i < len)
        {
            cmn = this.GetCommonString(cmn, strs[i]);
            i++;
        }
        
        return cmn;
        
    }
    
    public string GetCommonString(string str1, string str2)
    {
        if(str1.Length == 0 || str2.Length == 0)
        {
            return "";
        }
        
        int len = str1.Length;
        if(str2.Length < str1.Length)
        {
            len = str2.Length;    
        }
        
        int counter = 0;
        char[] s1CharArr = str1.ToCharArray();
        char[] s2CharArr = str2.ToCharArray();
        
        while(counter < len)
        {
            if(s1CharArr[counter] != s2CharArr[counter])
            {
                break;
            }
            
            counter++;
        }
        
        return str1.Substring(0, counter);
    }
}