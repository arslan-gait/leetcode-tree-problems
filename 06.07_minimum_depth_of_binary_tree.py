# https://leetcode.com/problems/minimum-depth-of-binary-tree/
from collections import deque
class Solution:
    # time complexity  - O(nodes(root)) to check all nodes
    # space complexity - O(nodes(root))
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level += 1
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left is None and cur.right is None:
                    return level
                if cur.right is not None:
                    queue.append(cur.right)
                if cur.left is not None:
                    queue.append(cur.left)
        return -1
