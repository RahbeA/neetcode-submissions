class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        tl = list(t)
        sl.sort()
        tl.sort()

        if len(sl) != len(tl):
            return False
        else:
            if sl != tl:
                return False
        return True