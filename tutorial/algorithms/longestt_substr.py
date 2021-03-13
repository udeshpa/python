#Given a string s, find the length of the longest substring without repeating characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        d = {}

        substrdict = {}

        currentmark = 0
        for i in range(0, n):
            print(f'{i}, {d} {currentmark}')
            if s[i] not in d:
                d[s[i]] = True
                continue

            substrdict[currentmark] = i-currentmark

            while True:
                d.pop(s[currentmark])
                currentmark = currentmark + 1
                if s[i] not in d or currentmark == i:
                    d[s[i]] = True
                    break
                print(f'current mark {currentmark}')
                substrdict[currentmark] = i - currentmark

        substrdict[currentmark] = i - currentmark + 1

        return substrdict;


sol = Solution()

substrs = sol.lengthOfLongestSubstring("abcabcbbb")
substrs = {k: v for k, v in sorted(substrs.items(), key=lambda item: item[1], reverse=True)}
print(substrs)









