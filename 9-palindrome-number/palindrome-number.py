class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers and numbers ending with 0 (but not 0 itself) aren't palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10
        
        # Even-length: x == reversed_half
        # Odd-length: x == reversed_half // 10 (middle digit ignored)
        return x == reversed_half or x == reversed_half // 10
