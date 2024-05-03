class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=collections.defaultdict(list)

        def getKey(word):
            freq=collections.defaultdict(int)

            for c in word:
                freq[c]+=1
            key=""
            for i in range(26):
                c=chr(ord('a')+i)
                key=key+c+","+str(freq[c])+","
            
            return key
        
        for word in strs:
            anagrams[getKey(word)].append(word)
        
        res=[]
        for key in anagrams:
            res.append(anagrams[key])
        
        return res
