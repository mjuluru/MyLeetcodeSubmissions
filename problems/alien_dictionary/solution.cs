public class Solution {
    Dictionary<char, IList<char>> adjList;
    Dictionary<char, bool> visited;
    IList<char> res;
    
    public string AlienOrder(string[] words) {
        res = new List<char>();
        adjList = new Dictionary<char, IList<char>>();
        
        foreach( var wd in words)
        {
            foreach(var ch in wd)
            {
                if(!adjList.ContainsKey(ch))
                {
                    var temp = new List<char>();
                    adjList.Add(ch, temp);
                }
            }
        }
        
        for(int i = 1; i<words.Length; i++)
        {
            string first = words[i-1]; 
            string sec = words[i];
            int minLen = Math.Min(sec.Length, first.Length);
            if(first.Length > sec.Length && first.Substring(0, minLen).Equals(sec.Substring(0, minLen)) == true)
            {
                return "";
            }
            
            Console.WriteLine("first: " + first + ", sec: " + sec);
            for(int j=0; j<minLen; j++)
            {
                Console.WriteLine("first: " + first[j] + ", sec: " + sec[j]);
                if(first[j] != sec[j])
                {
                    if(adjList.ContainsKey(first[j]))
                    {
                        adjList[first[j]].Add(sec[j]);
                    }
                    else
                    {
                        var temp = new List<char>();
                        temp.Add(sec[j]);
                        adjList.Add(first[j], temp);
                    }
                    
                    break;
                }
            }
        }
        
        visited = new Dictionary<char, bool>();
        
        
        foreach(var ch in adjList.Keys)
        {
            if(depth(ch))
            {
                return "";
            }
        }
        
        return new String(string.Join("", res).ToCharArray().Reverse().ToArray());
    }
    
    public bool depth(char ch)
    {
        if(visited.ContainsKey(ch))
        {
            return visited[ch];
        }
        
        visited.Add(ch, true);
        foreach(var nei in adjList[ch])
        {
            if(depth(nei))
            {
                return true;
            }
        }
        
        visited[ch] = false;
        res.Add(ch);
        
        return false;
    }
}