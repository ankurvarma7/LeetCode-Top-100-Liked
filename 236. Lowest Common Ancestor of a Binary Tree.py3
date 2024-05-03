class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        if root==p or root==q:
            return root
        
        else:
            left=self.lowestCommonAncestor(root.left,p,q)
            right=self.lowestCommonAncestor(root.right,p,q)

            if left and right:
                return root
            if left:
                return left
            return right
