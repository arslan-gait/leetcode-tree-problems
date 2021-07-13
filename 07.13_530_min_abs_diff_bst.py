# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
class Solution:
    
    def __init__(self):
        self.ans  = float('inf')
        self.prev = -1
    
    # recursive
    # time complexity  - O(nodes(root)) to check every node
    # space complexity - O(height(root))
    def getMinimumDifference(self, root: TreeNode) -> int:
        
        if root is None:
            return self.ans
        
        self.getMinimumDifference(root.left)
        
        if self.prev != -1 and root.val - self.prev < self.ans:
            self.ans = root.val - self.prev
        
        self.prev = root.val
        
        self.getMinimumDifference(root.right)
        
        return self.ans
