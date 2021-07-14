# https://leetcode.com/problems/find-mode-in-binary-search-tree/submissions/

class Solution:
    
    # recursive
    # time & space complexity O(nodes(root))
    def findMode(self, root: TreeNode) -> List[int]:
        
        cnt, maxCnt, prev = 1, 0, 100_001
        modes = []

        
        def handleVal(val: int):
            
            nonlocal cnt, maxCnt, prev, modes
            
            if val == prev:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > maxCnt:
                maxCnt = cnt
                modes = [val]
            elif cnt == maxCnt:
                modes.append(val)
            
            prev = val
        
        
        # in-order traversal
        def visit(node: TreeNode):
            
            if node is None:
                return
            
            visit(node.left)
            handleVal(node.val)                        
            visit(node.right)
        
        
        visit(root)
        
        return modes

    
    # recursive (same as above, but no extra space)
    # time complexity  - O(nodes(root))
    # space complexity - O(height(root))
    def findMode(self, root: TreeNode) -> List[int]:
        
        cnt, maxCnt, prev = 1, 0, 100_001
        modes = []

        
        def handleVal(val: int, isSecond: bool):
            
            nonlocal cnt, maxCnt, prev
            
            if val == prev:
                cnt += 1
            else:
                cnt = 1
            
            if cnt > maxCnt:
                maxCnt = cnt
                
            if isSecond and cnt == maxCnt:
                modes.append(val)
            
            prev = val
        
        
        # in-order traversal
        def visit(node: TreeNode, isSecond: bool):
            
            if node is None:
                return
            
            visit(node.left, isSecond)
            handleVal(node.val, isSecond)                        
            visit(node.right, isSecond)           
        
        
        visit(root, False)
        cnt, prev = 1, 100_001
        visit(root, True)
        
        return modes
