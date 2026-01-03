# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node,currsum):
            if not node:
                return False
            currsum += node.val
            if not node.left and not node.right:
                print(currsum)
                return targetSum == currsum

            return dfs(node.left, currsum) or dfs(node.right, currsum)

        return dfs(root,0)
#using bfs 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root :
            return False

        queue = deque([(root,targetSum - root.val)])

        while queue:
            node, currSum = queue.popleft()
            # base condition
            if not node.left and not node.right and currSum == 0:
                return True
            if node.left:
                queue.append((node.left , currSum - node.left.val))
            if node.right:
                queue.append((node.right, currSum - node.right.val))
        
        return False