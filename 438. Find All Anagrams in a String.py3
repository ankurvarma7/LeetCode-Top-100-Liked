class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        freqInWin=collections.defaultdict(int)
        freqInP=collections.defaultdict(int)

        def matchFreq():
            for ch in freqInP:
                if freqInP[ch]!=freqInWin[ch]:
                    return False
            
            return True
        
        for ch in p:
            freqInP[ch]+=1
        
        for i in range(len(p)):
            freqInWin[s[i]]+=1
        
        ans=[]
        if matchFreq():
            ans.append(0)
        
        st=0
        en=len(p)

        while(en<len(s)):
            freqInWin[s[en]]+=1
            freqInWin[s[st]]-=1
            en+=1
            st+=1
            if matchFreq():
                ans.append(st)
            
        return ans
