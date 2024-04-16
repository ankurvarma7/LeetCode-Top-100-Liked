class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def solve(node):
            if node is None:
                return (0,-1)
            
            lstMaxDia,lstEdgeLen=solve(node.left)
            rstMaxDia,rstEdgeLen=solve(node.right)
            
            currMaxDia=max(lstMaxDia,rstMaxDia,2+lstEdgeLen+rstEdgeLen)
            currEdgeLen=1+max(lstEdgeLen,rstEdgeLen)
            return (currMaxDia,currEdgeLen)

        maxDia,edgeLen=solve(root)

        return maxDia
