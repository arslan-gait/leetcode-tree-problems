# https://leetcode.com/problems/construct-string-from-binary-tree/
class Solution:
    
    # recursive
    # time complexity  - O(nodes(root)) need to traverse every node
    # space complexity - O(nodes(root)) to store the string
    def tree2str(self, root: TreeNode) -> str:
        if root is None:
            return ''
        
        s = str(root.val)
        
        if root.left is not None:
            s = f'{s}({self.tree2str(root.left)})'
        elif root.right is not None:
            s = f'{s}()'
        if root.right is not None:
            s = f'{s}({self.tree2str(root.right)})'
            
        return s
    
    
    # iterative
    # time complexity  - O(nodes(root)^2) need to traverse every node * set worst case
    # space complexity - O(nodes(root)) to store visited nodes
    def tree2str2(self, root: TreeNode) -> str:
        if root is None:
            return ''
        ans = ''
        stack = [root]
        visited = set()
        while stack:
            cur = stack[-1]
            if cur in visited:          # O(1)
                ans = f'{ans})'
                stack.pop()
            else:
                visited.add(cur)        # O(1)
                ans = f'{ans}({cur.val}'
                if cur.right is not None and cur.left is None:
                    ans = f'{ans}()'
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)
        return ans[1:-1]
