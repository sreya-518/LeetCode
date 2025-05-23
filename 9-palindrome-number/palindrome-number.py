class Solution:
    def isPalindrome(self, x: int) -> bool:
        orginal = x
        reverse = 0
        while x > 0:
            digit = x % 10
            x = x // 10
            reverse = reverse * 10 + digit
        return True if reverse == orginal else False


