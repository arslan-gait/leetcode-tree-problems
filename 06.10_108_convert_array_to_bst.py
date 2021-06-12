# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/submissions/
class Solution:
    
    # recursive
    # time complexity  - O(len(nums))
    # space complexity - O(len(nums)) to store new tree
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def helper(left: int, right: int) -> TreeNode:
            if right < left:
                return None
            mid = (right - left) // 2 + left
            t = TreeNode(nums[mid])
            t.left = helper(left, mid - 1)   # T(n/2) -> O(logn)
            t.right = helper(mid + 1, right) # T(n/2) -> O(logn)
            return t
        
        return helper(0, len(nums) - 1)
