class Solution:
    def rob(self, nums: List[int]) -> int:
        s=0
        s1 = 0
        for i in nums:
            t=max(s+i,s1)
            s=s1
            s1=t
        return t
        