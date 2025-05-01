class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        result = 0
        negative = x<0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x = x//10

            if result > (INT_MAX - digit) // 10:
                return 0
            result = (result*10)+digit
        return -result if negative else result


        