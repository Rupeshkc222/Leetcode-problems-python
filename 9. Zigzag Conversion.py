class Solution:
    def convert(self, s: str, numRows: int) -> str:
        sl=0
        if len(s) <=2 or numRows==1 or len(s)<=numRows:
            return(s)
        rl,cl=numRows,len(s)//2
        res=['']*numRows
        r_c,c_c=numRows,0
        while sl<len(s):
            for r in range(numRows):
                res[r]=res[r]+s[sl]
                sl=sl+1   
            check=True
            r_c=r
            while check==True and sl<len(s):
                r_c,c_c=r_c-1,c_c+1
                if r_c==0:
                    check=False
                else:
                    res[r_c]=res[r_c]+s[sl]
                    sl=sl+1
            if len(s)-sl<numRows:
                numRows=len(s)-sl
        return(''.join(res)) 

'''Input: s = "PAYPALISHIRING", numRows = 4
   Output: "PINALSIGYAHRPI"
    Explanation:
    P     I    N
    A   L S  I G
    Y A   H R
    P     I
'''        