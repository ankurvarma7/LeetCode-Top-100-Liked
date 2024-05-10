class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        i=0
        j=0

        l=-1
        r=-1
        ans=0
        freqT={}
        freqS={}

        for c in t:
            if c not in freqT:
                freqT[c]=0
            freqT[c]+=1
        matched=0
        while j<len(s):
            if s[j] not in freqS:
                freqS[s[j]]=0
            freqS[s[j]]+=1
            if s[j] in freqS and s[j] in freqT and freqS[s[j]]==freqT[s[j]]:
                matched+=1
            while matched==len(freqT):
                if ans==0 or ans>(j-i+1):
                    l=i
                    r=j
                    ans=j-i+1
                freqS[s[i]]-=1
                if s[i] in freqS and s[i] in freqT and freqS[s[i]]<freqT[s[i]]:
                    matched-=1
                i+=1
            j+=1
        
        if ans==0:
            return ""
        return s[l:r+1]
