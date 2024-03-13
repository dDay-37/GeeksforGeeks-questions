//{ Driver Code Starts
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
            int n = Integer.parseInt(br.readLine().trim());
            int[][] mat = new int[n][n];
            String[] S = br.readLine().trim().split(" ");
            int i = 0;
            int j = 0;
            for(int k = 0; k < S.length; k++){
                mat[i][j] = Integer.parseInt(S[k]);
                j++;
                if(j == n){
                    i++;
                    j = 0;
                }
            }
            Solution obj = new Solution();
            int[] ans = obj.matrixDiagonally(mat);
            for(int it = 0; it < ans.length; it++){
                System.out.print(ans[it] + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution {
    public int[] matrixDiagonally(int[][] mat) {
         int row=0,col=0,n=mat.length;
         boolean isReverse=false;
         int ans[] = new int[n*n];
         int index=0;
         while(col<n){
             ArrayList<Integer> temp = new ArrayList<>();
             int i=row,j=col;
             while(i<n && j<n && i>=0 && j>=0){
                 temp.add(mat[i][j]);
                 i--;
                 j++;
             }
             if(isReverse)Collections.reverse(temp);
             for(int k=0;k<temp.size();k++){
                 ans[index++]=temp.get(k);
             }
             if(row!=n-1){
                 row++;
                 col=0;
             }
             else{
                 col++;
             }
             isReverse=!isReverse;
         }
         return ans;
    }
}
