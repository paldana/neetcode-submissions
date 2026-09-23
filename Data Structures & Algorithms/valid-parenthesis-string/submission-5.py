## Stack Solution Practice
class Solution:
    def checkValidString(self, s: str) -> bool:
        # maintain 2 stacks to keep track of the chars we see in s
        left = []
        star = []

        for i, c in enumerate(s):
            if c == "(":
                left.append(i)      # appending index 
            elif c == "*":
                star.append(i)
            else:   # c == ")"
                if not left and not star:
                    return False
                elif left:      # if there's any ( left - pop this first before star since it's a wildcard
                    left.pop()
                else:
                    star.pop()
        
        # after the for loop, check if there are any ( and * left
        while left and star:
            # this is where the indices comes to play 
            # - if at any point the index of the ( is greater than *, that means * came before ( 
            #   and the star can only be either another '(' or an empty string, hence the string is INVALID
            if left.pop() > star.pop():
                return False
        
        # at this point, it's possible that there's ( left in the stack so check if there are remaining to determine validity of string
        return not left
        
        