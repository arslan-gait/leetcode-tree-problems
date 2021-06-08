#https://leetcode.com/problems/merge-two-binary-trees/
class Solution:
    # recursive
    # time complexity  - O(min(nodes(p), nodes(q))
    # space complexity - O(min(height(p), height(q)))
    def mergeTrees(self, p: TreeNode, q: TreeNode) -> TreeNode:
        if p is None:
            return q
        if q is None:
            return p
        p.val += q.val
        p.left = self.mergeTrees(p.left, q.left)
        p.right = self.mergeTrees(p.right, q.right)
        return p
    
    # iterative
    # time complexity  - O(min(nodes(p), nodes(q))
    # space complexity - O(min(height(p), height(q)))
    def mergeTrees2(self, p: TreeNode, q: TreeNode) -> TreeNode:
        if p is None:
            return q
        stack = [(p, q)]
        
        while stack:
            first, second = stack.pop()
            if first is None or second is None:
                continue
            first.val += second.val
            
            if first.left is not None:
                stack.append((first.left, second.left))
            else:
                first.left = second.left

            if first.right is not None:
                stack.append((first.right, second.right))
            else:
                first.right = second.right

        return p
