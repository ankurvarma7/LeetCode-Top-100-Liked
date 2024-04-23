class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq=collections.defaultdict(int)
        windowFreq=collections.defaultdict(int)
        def getDiff():
            diff=0
            for c in windowFreq:
                diff=max(diff,freq[c]-windowFreq[c])
            
            return diff
        
        for i in range(len(s)):
            freq[s[i]]+=1
        
        ans=[]
        index=0
        prev=0
        while index<len(s):
            windowFreq[s[index]]+=1
            diff=getDiff()

            if diff==0:
                windowFreq=collections.defaultdict(int)
                ans.append(index+1-prev)
                prev=index+1
            index+=1
            
        return ans
