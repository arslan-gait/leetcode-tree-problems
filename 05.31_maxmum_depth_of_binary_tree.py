# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque

class Solution:
  
  # iterative
  def maxDepth(self, root: TreeNode) -> int:
    if root == None:
      return 0
    nodes = deque()
    nodes.append(root)
    level = 0
    while nodes:
      for _ in range(len(nodes)):
        cur = nodes.popleft()
        if cur.left != None:
          nodes.append(cur.left)
        if cur.right != None:
          nodes.append(cur.right)
      level += 1
    return level

  # recursive
  def maxDepth2(self, root: TreeNode) -> int:
    if root == None:
      return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
