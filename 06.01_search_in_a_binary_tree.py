# https://leetcode.com/problems/search-in-a-binary-search-tree/
class Solution:
    
    # recursive
    # space and time complexity - O(height(root))
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return None
        elif root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        # checking val in the end reduces the number of comparisons
        else:
            assert(root.val == val)
            return root
    
    # iterative
    # space complexity - O(1)
    # time complexity  - O(height(root))
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
