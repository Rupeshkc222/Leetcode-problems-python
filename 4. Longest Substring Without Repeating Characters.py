class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        re=[]
        re_num=0
        for i in s:
            if i in re:
                if len(re)>re_num:
                    re_num=len(re)
                re=re[re.index(i) +1 :]
                re.append(i)
            else:
                re.append(i)
        if re_num >len(re):
            return(re_num)
        else:
            return(len(re))

'''Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''