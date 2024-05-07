class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q4BFS=deque()
        q4BFS.append(root)
        res=[]

        while q4BFS:
            size=len(q4BFS)
            for i in range(size):
                node=q4BFS.popleft()

                if i == size-1:
                    res.append(node.val)
                
                if node.left:
                    q4BFS.append(node.left)
                if node.right:
                    q4BFS.append(node.right)
        return res
