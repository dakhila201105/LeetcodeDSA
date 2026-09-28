# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.m_no_count = 0
        
        def cal_st(node):
            if not node:
                return 0, 0
            
            l_sum, l_count = cal_st(node.left)
            r_sum, r_count = cal_st(node.right)
            
            c_sum = l_sum + r_sum + node.val
            c_count = l_count + r_count + 1
            
            if c_sum // c_count == node.val:
                self.m_no_count += 1
                
            return c_sum, c_count

        cal_st(root)
        return self.m_no_count