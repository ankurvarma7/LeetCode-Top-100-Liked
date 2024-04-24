class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]

        palindromes=set()

        for i in range(len(s)):
            for j in range(i,len(s)):
                st=i
                en=j

                while st<=en:
                    if s[st]==s[en]:
                        st+=1
                        en-=1
                    else:
                        break
                    
                if st>=en:
                    palindromes.add((i,j))
        
        def isPalindrome(st,en):
            if (st,en) in palindromes:
                return True
            
            return False

        def solve(index):
            if index==len(s):
                res.append(curr.copy())
                return
            
            for i in range(index,len(s)):
                if isPalindrome(index,i):
                    curr.append(s[index:i+1])
                    solve(i+1)
                    curr.pop()
                
        solve(0)
        return res
