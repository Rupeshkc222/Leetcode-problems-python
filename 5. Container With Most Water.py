class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=[]
        l,r=0,len(height)-1
        while l<r and r>l:
            m_in=min(height[l],height[r])
            res.append(m_in*(r-l))    #find the area of both lines
            if height[r] > height[l]:
                l=l+1
            elif height[r] < height[l]:
                r=r-1
            else:
                l,r=l+1,r-1
        return max(res)

'''Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.'''        