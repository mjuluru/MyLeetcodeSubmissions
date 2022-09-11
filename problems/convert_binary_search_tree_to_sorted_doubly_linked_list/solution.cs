/*
// Definition for a Node.
public class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val) {
        val = _val;
        left = null;
        right = null;
    }

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
}
*/

public class Solution {
    Node head = null;
    Node tail = null;
    public Node TreeToDoublyList(Node root) {
        if(root == null)
            return null;
        
        this.Dfs(root);
        
        head.left = tail;
        tail.right = head;
        
        return head;
    }
    
    public void Dfs(Node root) {
        if(root == null) 
            return;
        
        this.Dfs(root.left);
        
        if(tail == null) {
            head = root;
            tail = root;
        }
        else
        {
            tail.right = root;
            root.left = tail;
            tail = root;
        }
        
        this.Dfs(root.right);
    }
}