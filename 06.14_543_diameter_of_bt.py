class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        ans = 0
        
        def getHeight(node: TreeNode) -> int:
            if node is None:
                return 0
            leftH = getHeight(node.left)
            rightH = getHeight(node.right)
            nonlocal ans
            ans = max(ans, leftH + rightH)
            return max(leftH, rightH) + 1
        
        getHeight(root)
        return ans

    def diameterOfBinaryTree2(self, root: TreeNode) -> int:
        from enum import Enum, auto

        class State(Enum):
            NOT_VISITED = auto()
            VISITED = auto()

        class MutableInt:
            def __init__(self, value: int):
                self.value = value
            
        ans = 0
        toProcess = [(root, MutableInt(0), State.NOT_VISITED, MutableInt(0), MutableInt(0))]
        while len(toProcess) > 0:
            (node, height, state, leftH, rightH) = toProcess.pop()
            if state == State.NOT_VISITED:
                if node is None:
                    height.value = 0
                else:
                    toProcess.append((node, height, State.VISITED, leftH, rightH))
                    toProcess.append((node.left, leftH, State.NOT_VISITED, MutableInt(0), MutableInt(0)))
                    toProcess.append((node.right, rightH, State.NOT_VISITED, MutableInt(0), MutableInt(0)))
            else:
                ans = max(ans, leftH.value + rightH.value)
                height.value = max(leftH.value, rightH.value) + 1
        return ans
