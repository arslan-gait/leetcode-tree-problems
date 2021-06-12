# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/
class Solution:
    
    def __init__(self):
        self.ans = -1

    # recursive
    # time & space complexity - O(nodes(root))
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
        def visit(node: TreeNode):
            if node is None:
                return
            
            if node.val > root.val:
                if self.ans == -1 or node.val < self.ans:
                    self.ans = node.val
                return
            visit(node.left)
            visit(node.right)
        
        visit(root)
        return self.ans
