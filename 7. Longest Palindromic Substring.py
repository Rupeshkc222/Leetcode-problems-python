class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        end=1
        m_len=1
        for i in range(1,len(s)):
            l1=i-1
            h1=i
            while(l1>=0 and h1<len(s) and s[l1]==s[h1]):
                if h1-l1+1>m_len:
                    start=l1
                    m_len=h1-l1+1
                    end=h1+1
                l1=l1-1
                h1=h1+1
            l1=i-1
            h1=i+1    
            while(l1>=0 and h1<len(s) and s[l1]==s[h1]):
                if h1-l1+1>m_len:
                    start=l1
                    m_len=h1-l1+1
                    end=h1+1   
                l1-=1
                h1+=1
        return(s[start:end])
'''Input: s = "babad"
    Output: "bab"
    Explanation: "aba" is also a valid answer.'''     