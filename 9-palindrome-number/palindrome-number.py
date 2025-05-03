class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # Find the divisor to extract the leftmost digit
        def get_divisor(x):
            div = 1
            while x >= 10 * div:
                div *= 10
            return div

        def helper(x, div):
            if x == 0:
                return True
            left = x // div
            right = x % 10
            if left != right:
                return False
            # Remove the first and last digits
            x = (x % div) // 10
            div = div // 100
            return helper(x, div)

        return helper(x, get_divisor(x))
