class Solution:
    def reverse(self, x: int) -> int:
        num=x
        if num <0:
            num=num*(-1)
        num=int(str(num)[::-1])
        if x<0:
            num=num*(-1)
        if num >(2**31)-1 or num<-1*(2**31):
            return 0
        return num
'''
Input: x = 123
Output: 321

Assume the environment does not 
allow you to store 64-bit integers (signed or unsigned).'''