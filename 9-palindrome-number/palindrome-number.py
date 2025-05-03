class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 

        def reverse(num, rev=0):
            if num == 0:
                return rev
            digit = num % 10
            return reverse(num // 10, rev * 10 + digit)

        return x == reverse(x)
