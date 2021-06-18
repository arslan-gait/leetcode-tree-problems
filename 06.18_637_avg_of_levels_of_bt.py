# https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution:
    
    # iterative - BFS
    # time complexity  - O(nodes(root))
    # space complexity - O(nodes(root))
    def averageOfLevels1(self, root: TreeNode) -> List[float]:
        ans = []
        curLevel = [root]
        
        while curLevel:
            nextLevel = []
            curAvg, curLen = 0, len(curLevel)
             
            for node in curLevel:
                curAvg += node.val
                if node.left is not None:
                    nextLevel.append(node.left)
                if node.right is not None:
                    nextLevel.append(node.right)
            
            curLevel = nextLevel
            ans.append(curAvg / curLen)
        
        return ans
    
    # recursive - DFS
    # time complexity  - O(nodes(root))
    # space complexity - O(height(root))
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        levels = []
        
        def dfs(root: TreeNode, level: int):
            if root is None:
                return
            
            nonlocal levels
            
            if level < len(levels):
                nodesNum, nodesSum = levels[level]
                levels[level] = (1 + nodesNum, root.val + nodesSum)
            else:
                levels.append((1, root.val))
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 0)
        for i, v in enumerate(levels):
            levels[i] = v[1]/v[0]
        return levels
