# https://leetcode.com/problems/symmetric-tree/
class Solution:
    
    # recursive
    # space and time complexity - O(min(height(p), height(q)))
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)
    
    def helper(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and \
            self.helper(p.left, q.right) and \
            self.helper(p.right, q.left)
    
    # iterative
    # space and time complexity - O(min(height(p), height(q)))
    def isSymmetric2(self, root: TreeNode) -> bool:
        stack = [(root, root)]
        while stack:
            first, second = stack.pop()
            if first is None and second is None:
                continue
            if first is None or second is None:
                return False
            assert(first is not None and second is not None)
            if first.val != second.val:
                return False
            stack.append((first.right, second.left))
            stack.append((first.left, second.right))
        return True
