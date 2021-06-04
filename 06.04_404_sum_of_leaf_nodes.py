# https://leetcode.com/problems/sum-of-left-leaves/submissions/
class Solution:
    
    # recursive
    # time complexity  - O(nodes(root)) since we need to traverse every node
    # space complexity - O(height(root)) for storing the call stack
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return self.helper(root.left, True) + self.helper(root.right, False)
    
    def helper(self, root: TreeNode, isLeft: bool) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            if isLeft:            
                return root.val
            else:
                return 0
        
        return self.helper(root.left, True) + self.helper(root.right, False)

    # iterative
    # time complexity  - O(nodes(root)) since we need to traverse every node
    # space complexity - O(nodes(root)) 
    def sumOfLeftLeaves2(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 0
        level = [(root, False)]
        while level:
            nxtLevel = []
            for node, isLeft in level:
                if node.left is None and \
                    node.right is None and \
                    isLeft:
                        ans += node.val
                if node.left is not None:
                    nxtLevel.append((node.left, True))
                if node.right is not None:
                    nxtLevel.append((node.right, False))
            level = nxtLevel
        return ans

    # iterative 2
    # time complexity  - O(nodes(root)) since we need to traverse every node
    # space complexity - O(height(root)) for storing the call stack
    def sumOfLeftLeaves3(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 0
        stack = [(root, False)]
        while stack:
            node, isLeft = stack.pop()
            if node.left is None and \
                node.right is None and \
                isLeft:
                    ans += node.val
            if node.left is not None:
                stack.append((node.left, True))
            if node.right is not None:
                stack.append((node.right, False))
        return ans
