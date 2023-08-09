class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1){
            return strs[0];
        }
        String prefix = "";
        for(int i=1; i<strs.length;i++){
            int j = 0;
            while((j<strs[i].length()) && (j<strs[i-1].length())){
                if( !prefix.isEmpty() && j<prefix.length()){
                    if(strs[i].charAt(j) != prefix.charAt(j)){
                        break;
                    }
                }
                else{
                    if (strs[i].charAt(j) != strs[i-1].charAt(j)){
                        break;
                    }
                }
                j += 1;
            }
            String x1 = strs[i].substring(0,j);
            String x3 = strs[i-1].substring(0,j);
            if ( i==1 && x1.equals(x3)){
                prefix = x1;
            }
            else{
                j = Math.min(prefix.length(),j);
                String x2 = prefix.substring(0,j);
                if (x1.equals(x2)){
                    prefix = x1;
                }
            }
        }
        return prefix;
    }
}