# https://leetcode.com/problems/average-of-levels-in-binary-tree/
class Solution:
    
    # iterative - BFS
    # time complexity  - O(nodes(root))
    # space complexity - O(nodes(root))
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
    # time complexity  - Theta(nodes(root)) on average, O(nodes(root)^2) worst due to dict operations
    # space complexity - O(height(root))
    def averageOfLevels2(self, root: TreeNode) -> List[float]:
        
        m = {}
        
        def dfs(root: TreeNode, level: int):
            if root is None:
                return
            
            nonlocal m
            
            if level in m:
                numNodes, nodesVal = m[level]
                m[level] = (1 + numNodes, root.val + nodesVal)
            else:
                m[level] = (1, root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
        
        dfs(root, 1)
        return [m[k][1]/m[k][0] for k in m]        
