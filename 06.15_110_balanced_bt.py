# https://leetcode.com/problems/balanced-binary-tree/submissions/
class Solution:
    
    # recursive
    # time complexity  - O(nodes(root))
    # space complexity - O(height(root))
    def isBalanced1(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def checkTree(node: TreeNode) -> int:
            if node is None:
                return 0
            left = checkTree(node.left)
            right = checkTree(node.right)
            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1
            return max(right, left) + 1
    
        return checkTree(root) != -1
