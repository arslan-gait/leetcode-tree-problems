# https://leetcode.com/problems/same-tree/
from collections import deque

class Solution:
    # iterative
    # space and time complexity - O(nodes(p) + nodes(q))
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        queue = deque([(p,q)])
        
        while queue:
            curP, curQ = queue.popleft()
            if not curP and not curQ:
                continue
            if not curP or not curQ:
                return False
            if curP.val != curQ.val:
                return False
            
            queue.append((curP.left, curQ.left))
            queue.append((curP.right, curQ.right))

        return True
    
    # recursive
    # time complexity  - O(nodes(p) + nodes(q))
    # space complexity - O(height(p) + height(q))
    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
