class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        st=0
        en=0
        unique=set()
        while en<len(s):
            if s[en] in unique:
                while st<en and s[en] in unique:
                    unique.remove(s[st])
                    st+=1
            unique.add(s[en])
            res=max(res,en-st+1)
            en+=1
        
        return res
