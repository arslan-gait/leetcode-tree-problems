# https://leetcode.com/problems/leaf-similar-trees/submissions/
class Solution:
    
    # iterative
    # time complexity  - O(max(nodes(root1), nodes(root2)))
    # space complexity - O(nodes(root1) + nodes(root2)) to store leaf values
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def getLeafNodes(root: TreeNode) -> List[int]:
            res = []
            stack = [root]
            while stack:
                cur = stack.pop()
                if cur.left is None and cur.right is None:
                    res.append(cur.val)
                else:
                    if cur.right is not None:
                        stack.append(cur.right)
                    if cur.left is not None:
                        stack.append(cur.left)
            return res
        
        return getLeafNodes(root1) == getLeafNodes(root2)
