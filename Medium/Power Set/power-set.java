//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String s = br.readLine().trim();
            Solution ob = new Solution();
            List<String> ans = ob.AllPossibleStrings(s);
            for(String i: ans)
                System.out.print(i + " ");
            System.out.println();
            
        }
    }
}

// } Driver Code Ends


//User function Template for Java

class Solution
{
     void help(String s,int index,List<String> ans,StringBuilder temp){
	    if(index==s.length()){
	        if(temp.length()!=0)ans.add(temp.toString());
	        return;
	    }
	    help(s,index+1,ans,temp);
	    temp.append(s.charAt(index));
	    help(s,index+1,ans,temp);
	    temp.deleteCharAt(temp.length()-1);
	}
    public List<String> AllPossibleStrings(String s)
    {
        List<String> ans = new ArrayList<>();
        StringBuilder temp = new StringBuilder();
	    help(s,0,ans,temp);
	    Collections.sort(ans);
	    return ans;
    }
}
