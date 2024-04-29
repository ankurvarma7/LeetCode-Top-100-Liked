class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

        def solve(root):
            if root is None:
                return (-float('inf'),float('inf'),True)
            

            lstMax,lstMin,isLeftBST=solve(root.left)
            rstMax,rstMin,isRightBST=solve(root.right)

            if root.val>lstMax and root.val<rstMin and isLeftBST and isRightBST:
                return (max(lstMax,rstMax,root.val),min(lstMin,rstMin,root.val),True)
            else:
                return (max(lstMax,rstMax,root.val),min(lstMin,rstMin,root.val),False)
        
        greatest,smallest,isBST=solve(root)
        return isBST
