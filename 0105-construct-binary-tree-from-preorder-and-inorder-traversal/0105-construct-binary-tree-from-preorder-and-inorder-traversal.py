class Solution(object):
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))

            node = TreeNode(inorder[index])

            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index+1:])

            return node       