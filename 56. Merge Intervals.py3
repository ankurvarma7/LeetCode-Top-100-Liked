class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:x[0])
        res=[]
        st=intervals[0][0]
        en=intervals[0][1]
        for interval in intervals:
            if interval[0]<=en:
                en=max(en,interval[1])
            
            else:
                res.append([st,en])
                st=interval[0]
                en=interval[1]
        
        res.append([st,en])

        return res
