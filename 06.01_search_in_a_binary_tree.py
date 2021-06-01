# https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:
    
    # recursive
    # space complexity - Θ(height(root)) average, O(nodes(root)) worst
    # time complexity  - Θ(log(nodes(root))) average, O(nodes(root)) worst
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
    
    # iterative
    # space complexity - O(1)
    # time complexity  - Θ(log(nodes(root))) average, O(nodes(root)) worst
    def searchBST2(self, root: TreeNode, val: int) -> TreeNode:
        cur = root
        while cur:
            if cur.val == val:
                return cur
            elif cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        return cur
