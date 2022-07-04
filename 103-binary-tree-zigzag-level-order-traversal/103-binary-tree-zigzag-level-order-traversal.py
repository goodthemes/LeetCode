# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root: return res
        
        flag = 1
        q = collections.deque()
        q.append(root)
        while q:
            tmp = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                tmp.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if flag == 1:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            flag *= -1
            
        return res
                