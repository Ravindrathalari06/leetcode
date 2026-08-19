class Solution:
    # Function to remove all occurrences of the character from the string
    def removeCharacter(self, s, c):
        # code here
        res=""
        for i in s:
            if i==c:
                continue;
            res+=i
        return res
                 
              
        