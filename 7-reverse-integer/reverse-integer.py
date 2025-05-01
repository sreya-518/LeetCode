class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        result = 0
        negative = x<0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x//10
            result = (result*10)+digit
            if result > INT_MAX:
                return 0
        return -result if negative else result