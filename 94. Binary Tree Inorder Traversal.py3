class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr=root
        res=[]

        while curr:
            if curr.left is None:
                res.append(curr.val)
                curr=curr.right
            
            else:
                temp=curr.left
                while temp.right and temp.right!=curr:
                    temp=temp.right
                
                if temp.right:
                    temp.right=None
                    res.append(curr.val)
                    curr=curr.right
                
                else:
                    temp.right=curr
                    curr=curr.left
        

        return res
