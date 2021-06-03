# https://leetcode.com/problems/same-tree/
from collections import deque

class Solution:
    # iterative
    # space and time complexity - O(min(nodes(p), nodes(q)))
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while len(stack) > 0:
            first, second = stack.pop()
            if first is None and second is None:
                continue
            if first is None or second is None:
                return False
            assert(first is not None and second is not None)
            if first.val != second.val:
                return False
            stack.append((first.left, second.left))
            stack.append((first.right, second.right))
        return True
    
    # recursive
    # space and time complexity - O(min(nodes(p), nodes(q)))
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return \
            p.val != q.val and \
            self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)
