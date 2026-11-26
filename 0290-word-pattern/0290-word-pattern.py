class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict1={}
        dict2 = {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict1:
                dict1[pattern[i]]=words[i]
            elif dict1[pattern[i]]!=words[i]:
                return False
            if words[i] not in dict2:
                dict2[words[i]] = pattern[i]
            elif dict2[words[i]] != pattern[i]:
                return False
        return True