//{ Driver Code Starts
/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;
    
    public Node (int data){
        this.data = data;
        this.next = null;
    }
}

class GFG {
    static void printList(Node node) 
	{ 
		while (node != null) 
		{ 
			System.out.print(node.data + " "); 
			node = node.next; 
		} 
		System.out.println(); 
	}
	public static void main (String[] args) {
		Scanner sc  = new Scanner(System.in);
		int t = sc.nextInt();
		while(t-- > 0){
		    int n = sc.nextInt();
		    
		    Node head = new Node(sc.nextInt());
		    Node tail = head;
		    
		    for(int i=1; i<n; i++){
		        tail.next = new Node(sc.nextInt());
		        tail = tail.next;
		    }
		    Solution obj = new Solution();
		    head = obj.sort(head);
		    printList(head);
		}
	}
}

// } Driver Code Ends

class Solution {
    
    public Node sort(Node head){
         //your code here, return the head of the sorted list
         Node n1=head;
         Node n2=head.next;
         while(n2!=null){
             if(n1.data>n2.data){
                 int t=n1.data;
                 n1.data=n2.data;
                 n2.data=t;
             }
             n2=n2.next;
             if(n2==null){
                 n1=n1.next;
                 n2=n1.next;
             }
         }
         return head;
    }
 
 
 }
