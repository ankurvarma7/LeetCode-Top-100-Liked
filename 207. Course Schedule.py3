class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        incedentEdges=collections.defaultdict(int)
        adjList=collections.defaultdict(list)

        for prerequisite in prerequisites:
            a=prerequisite[0]
            b=prerequisite[1]

            adjList[b].append(a)
            incedentEdges[a]+=1
        q4BFS=deque()
        completed=set()
        for node in range(numCourses):
            if incedentEdges[node]==0:
                q4BFS.append(node)
                completed.add(node)
            
        while q4BFS:
            node=q4BFS.popleft()

            for nei in adjList[node]:
                incedentEdges[nei]-=1
                if incedentEdges[nei]==0:
                    q4BFS.append(nei)
                    completed.add(nei)
        
        return len(completed)==numCourses
