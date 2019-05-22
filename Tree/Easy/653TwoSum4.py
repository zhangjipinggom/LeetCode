# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):


    def dfs(self, tree):
        if not tree: return          # 停止递归
        self.dfs(tree.left)
        self.s.append(tree.val)
        self.dfs(tree.right)

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.s = []
        self.dfs(root)
        start, end = 0, len(self.s)-1
        while start != end:
            sumed = self.s[start] + self.s[end]
            if sumed == k:
                return True
            elif sumed > k:
                end -= 1
            else:
                start += 1
        return False




