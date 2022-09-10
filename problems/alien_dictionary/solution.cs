public class Solution {
    string res = "";
    Dictionary<char, bool> visit = new Dictionary<char, bool>();
    public string AlienOrder(string[] words) 
    {
        Dictionary<char, List<char>> map = new Dictionary<char, List<char>>();
        
        foreach(var wd in words) {
            foreach(var ch in wd) {
                if(!map.ContainsKey(ch)) {
                    //Console.WriteLine("aa: " + ch);
                    map.Add(ch, new List<char>());
                }
            }
        }
        
        for(int i=0; (i+1)<words.Length; i++) {
            string str1 = words[i];
            string str2 = words[i+1];
            
            if(str2.Length < str1.Length && str2.Equals(str1.Substring(0, str2.Length))) {
                return "";
            }

            for(int j=0; j<str1.Length && j<str2.Length; j++) {
                if(str1[j] != str2[j]) {
                    if(!map.ContainsKey(str1[j])) {
                        map.Add(str1[j], new List<char>());
                    }
                    if(str2[j] == 'c') {
                        Console.WriteLine("==== " + j  +"," + str1 + "," + str2);
                    }
                    map[str1[j]].Add(str2[j]);
                    
                    break;
                }
            }
        }
        
        foreach(var ch in map.Keys) {
            Console.WriteLine("---" + ch + "," + string.Join("", map[ch]));
        }
        
        foreach(var ch in map.Keys) {
            Console.WriteLine("first char:: " + ch + ":" + string.Join("", map[ch]));
            if(this.Recursion(map, ch, visit)) {
                return "";
            }
        }
        
        return new String(this.res.ToCharArray().Reverse().ToArray());
    }
    
    public bool Recursion(Dictionary<char, List<char>> map, char ch, Dictionary<char, bool> visit){
        Console.WriteLine("-------- does visit contains " + ch + "," + visit.ContainsKey(ch));
        if(visit.ContainsKey(ch)) {
            return visit[ch];
        }

        visit.Add(ch, true);
        foreach(char nei in map[ch]) {
            Console.WriteLine("--------" + nei);
            if(this.Recursion(map, nei, visit))
                return true;
        }
        
        visit[ch] = false;
        this.res += ch;
        Console.WriteLine("printed char " + ch);
        return visit[ch];
    }
}