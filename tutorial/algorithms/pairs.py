class Solution(object):
    def numpairs(self, x, y):
        count = 0
        for i in x:
            for j in y:
                if pow(i, j) > pow(j, i):
                    count = count +1
        return count


sol = Solution()
ret = sol.numpairs([2,1,6], [1,5])
print(ret)

ret = sol.numpairs([2, 3, 4, 5], [1, 2, 3])
print(ret)
