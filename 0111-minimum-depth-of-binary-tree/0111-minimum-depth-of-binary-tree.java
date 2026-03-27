/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int minDepth(TreeNode root) {
        return countDepth(root);
    }

    private int countDepth(TreeNode node){
        if(node == null) return 0;

        if(node.left == null) {
            return countDepth(node.right) + 1;
        }

        if(node.right == null) {
            return countDepth(node.left) + 1;
        }

        return Math.min(countDepth(node.left), countDepth(node.right)) + 1;
    }
}