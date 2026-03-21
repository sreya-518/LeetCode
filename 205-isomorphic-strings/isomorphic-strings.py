class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1, m2 = {}, {}
        for i in range(len(s)): #0,1,2
            c1, c2= s[i], t[i]
            if (c1 in m1 and m1[c1] != c2) or (c2 in m2 and m2[c2] != c1):
                return False
            m1[c1] = c2
            m2[c2] = c1

        return True



        