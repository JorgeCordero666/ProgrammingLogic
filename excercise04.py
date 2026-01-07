# Give two strings s and t, return true  if t is an anagram of s, and false otherwise

class Solution(object):
    def isAnagramLessOptimatized(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        for letra in s:
            if s.count(letra) != t.count(letra):
                return False

        return True

    def isAnagramOptimatized(s, t):
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count:
                return False
            count[c] -= 1

        return all(v == 0 for v in count.values())

            
sol = Solution()
print(sol.isAnagram('rat','car'))