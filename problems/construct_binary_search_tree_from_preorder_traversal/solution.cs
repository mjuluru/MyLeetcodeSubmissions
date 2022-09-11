/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    int ind = 0;
    public TreeNode BstFromPreorder(int[] preorder) {
        if(preorder == null)
            return null;
        
        return this.CreateBst(preorder, Int32.MinValue, Int32.MaxValue);
    }
    
    public TreeNode CreateBst(int[] pre, int low, int high) {
        if(ind == pre.Length) {
            return null;            
        }
        
        if(pre[ind] < low || pre[ind] > high)
            return null;
        
        var val = pre[ind];
        // Console.WriteLine(val);
        TreeNode node = new TreeNode(pre[ind]);
        ind++;
        node.left = this.CreateBst(pre, low, val);
        node.right = this.CreateBst(pre, val, high);
        
        
        
        return node;
    }
}