class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        s=0
        for i in nums:
            if i==1:
                c+=1
                s=max(s,c)
            else:
                c=0
        return s
        