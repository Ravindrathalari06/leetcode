class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
         hl=0
         s=0
         for i in range(len(gain)):
            s+=gain[i]
            hl=max(hl,s)
         return hl