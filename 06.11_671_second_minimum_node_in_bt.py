# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/
class Solution:
    
    def __init__(self):
        self.ans = -1

    # recursive
    # time complexity  - O(nodes(root))
    # space complexity - O(height(root))
    def findSecondMinimumValue2(self, root: TreeNode) -> int:
        
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
    
    # iterative BFS
    # time & space complexity - O(nodes(root))
    def findSecondMinimumValue3(self, root: TreeNode) -> int:
        ans = -1
        curLevel = [root]
        while curLevel:
            nextLevel = []
            for node in curLevel:
                if node.val > root.val:
                    if ans == -1 or node.val < ans:
                        ans = node.val
                    continue
                else:
                    if node.left is not None:
                        nextLevel.append(node.left)
                    if node.right is not None:
                        nextLevel.append(node.right)
            curLevel = nextLevel
        return ans

    # iterative DFS
    # time complexity  - O(nodes(root))
    # space complexity - O(height(root))
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        ans = -1
        stack = [root]
        while stack:
            node = stack.pop()
            
            if node.val > root.val:
                if ans == -1 or node.val < ans:
                    ans = node.val
                continue
            else:
                if node.left is not None:
                    stack.append(node.left)
                if node.right is not None:
                    stack.append(node.right)

        return ans
