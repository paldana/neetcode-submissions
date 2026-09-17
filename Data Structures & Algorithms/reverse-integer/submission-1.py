class Solution:
    def reverse(self, x: int) -> int:
        ## Iteration Solution - O(1) -- MATH SOLUTION - not a Bit Manipulation
        # given a SIGNED 32-bit integer range
        MIN = -2147483648  # -2^31, 0x80000000
        MAX = 2147483647  #  2^31 - 1, 0x7FFFFFFF

        res = 0
        while x:
            ## get the least significant digit by modding - fmod will get the sign of x; using % will get the sign of y in "x % y"
            digit = int(math.fmod(x, 10))      # i.e. x = 123 --> we get the ones digit number - digit = 3              ## (python dumb) -1 % 10 = 9
            x = int(x / 10)                    #      x = 123 --> we truncate the digit and update x to 12              ## (python dumb) -1 // 10 = -1

            # / - true division = always calculates the exact division and always returns a float, even if the numbers divide evenly.
            # // - floor division = divides the numbers and rounds down to the nearest whole integer (towards negative infinity)
            
            """ Check if the current res will be out of the signed 32-bit integer range
            
            1st check - res > MAX // 10  
                -> check if all the other 31-bit integer, not including the ones digit, is greater than the MAX's 31-bit integer, also without the ones digit.
                   
            
            i.e. 
            MIN = -2147483648  # -2^31, 0x80000000
            MAX = 2147483647  #  2^31 - 1, 0x7FFFFFFF

                Here, we're comparing the the res' 31-bit digits less the ones digit and the MIN's and MAX's
                    MIN = -214748364_
                    MAX = 214748364_


            2nd check - (res == MAX // 10 and digit > MAX % 10)
                -> this is to compare if the res' ones digit (digit) is greater than 7 for MAX 
                  or less than -8 for MIN. If they are, then it is out of range.

            """

            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0
            """ Slowly build the reversed digit, starting with the ones digit in the original value, x
                in the next iteration, we will multiply res by 10 to move the initially added number to a more significant digit
                i.e. Given x = 123 
                1st iteration - res = 0, digit = 3, x = 12
                                res = (0 * 10) + 3 = 3
                2nd iteration - res = 3, digit = 2, x = 1
                                res = (3 * 10) + 2 = 32
                3rd iteration - res = 32, digit = 1, x = 0
                                res = (32 * 10) + 1 = 321
                End of while loop since x = 0 
                                res = 321         -> we got out reversed number!
            """
            res = (res * 10) + digit            

        return res

## Math Solution
# Time Complexity - O(1)
# Space Complexity - O(1)
