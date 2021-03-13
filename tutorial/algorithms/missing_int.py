class Solution(object):
    def missing_int(self, ary, N):
          total = (N) * ( N+1)/2
          for i in ary:
              total = total - i

          print(total)


sol = Solution()
sol.missing_int([1,2,3], 4)
