# https://leetcode.com/problems/construct-string-from-binary-tree/
class Solution:
    
    # recursive - slow
    # time complexity  - O(nodes(root)^2) need to traverse every node plus string concat
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
    
    # recursive
    # time complexity  - O(nodes(root))
    # space complexity - O(nodes(root))
    def tree2str3(self, root: TreeNode) -> str:
        ans = []
        def visit(node: TreeNode) -> None: 
            if node is None:
                return
        ans.append(str(node.val))
        if node.left is not None or node.right is not None:
            ans.append(’(’)
            visit(node.left)
            ans.append(’)’)
        if node.right is not None: 
            ans.append(’(’)
            visit(node.right)
            ans.append(’)’)
        visit(root)
        return ’’.join(ans)
    
    
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
            if cur in visited:          # O(N)
                ans = f'{ans})'
                stack.pop()
            else:
                visited.add(cur)        # O(N)
                ans = f'{ans}({cur.val}'
                if cur.right is not None and cur.left is None:
                    ans = f'{ans}()'
                if cur.right is not None:
                    stack.append(cur.right)
                if cur.left is not None:
                    stack.append(cur.left)
        return ans[1:-1]
    
    # iterative
    # time complexity  - O(nodes(root))
    # space complexity - O(nodes(root))
    def tree2str(self, root: TreeNode) -> str:
        from enum import Enum, auto        
        class State(Enum):
            NOT_VISITED = auto()
            LEFT_VISITED = auto()
            RIGHT_VISITED = auto()
            
        ans = []
        toVisit = [(root, State.NOT_VISITED)]
        while len(toVisit) > 0:
            node, state = toVisit.pop()
            if state is State.NOT_VISITED:
                ans.append(str(node.val))
                if node.left is not None:
                    ans.append('(')
                    toVisit.append((node, State.LEFT_VISITED))
                    toVisit.append((node.left, State.NOT_VISITED))
                elif node.right is not None:
                    ans.append('()(')
                    toVisit.append((node, State.RIGHT_VISITED))
                    toVisit.append((node.right, State.NOT_VISITED))
            elif state is State.LEFT_VISITED:
                ans.append(')')
                if node.right is not None:
                    ans.append('(')
                    toVisit.append((node, State.RIGHT_VISITED))
                    toVisit.append((node.right, State.NOT_VISITED))
            else:
                assert(state is State.RIGHT_VISITED)
                ans.append(')')
        return ''.join(ans)

