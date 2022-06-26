public class Solution {
    public bool IsValid(string s) {
        int len = s.Length;
        if(s.Length == 0)
            return true;
        if(len == 1)
            return false;
        
        var chr = s.ToCharArray(); 
        Stack<char> stack = new Stack<char>();
        
        int i =0;
        while(i < len)
        {
            if(chr[i] == '{' || chr[i] == '(' || chr[i] == '[')
            {
                stack.Push(chr[i]);
            }
            
            if(chr[i] == '}' || chr[i] == ')' || chr[i] == ']')
            {
                if(stack.Count > 0)
                {
                    char peekedCh = stack.Peek();
                    if(peekedCh == '{' && chr[i] == '}')
                    {
                        stack.Pop();
                    }
                    else if(peekedCh == '[' && chr[i] == ']')
                    {
                        stack.Pop();
                    }
                    else if(peekedCh == '(' && chr[i] == ')')
                    {
                        stack.Pop();
                    }
                    else
                    {
                        return false;
                    }
                }
                else
                {
                    return false;
                }
            }
            
            i++;
        }
        
        if(stack.Count > 0)
        {
            return false;
        }
        
        return true;
    }
}