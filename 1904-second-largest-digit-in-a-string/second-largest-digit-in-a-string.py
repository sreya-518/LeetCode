class Solution:
    def secondHighest(self, s: str) -> int:
        first = second = -1
        for ch in s:
            if ch.isdigit():
                num = int(ch)
                if num > first:
                    second = first
                    first = num
                elif first > num > second:
                    second = num
        return second