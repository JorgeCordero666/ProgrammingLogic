# You are given two strings word01 and word02. Merge the strings by adding letter in alternating order,
# starting with word01. if a string is longer than the other, appened the additional letters onto the end of 
# the merged string
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0 

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i+= 1
        
        return ''.join(result)




