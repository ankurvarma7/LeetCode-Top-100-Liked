class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return root
        
        lst=root.left
        rst=root.right

        root.left=None
        root.right=self.flatten(lst)
        curr=root
        while curr.right:
            curr=curr.right
        
        curr.right=self.flatten(rst)

        return root
