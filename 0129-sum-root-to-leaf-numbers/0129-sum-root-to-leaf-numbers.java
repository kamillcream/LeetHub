class Solution {
    public int sumNumbers(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int curSum) {
        if(node == null) return 0;
        curSum = curSum * 10 + node.val;

        if(node.right == null && node.left == null) return curSum;
    

        return dfs(node.left, curSum) + dfs(node.right, curSum);
    }
}