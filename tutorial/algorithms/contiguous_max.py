class Solution(object):

    #[6, -4, 7, -8, 9, -50]
    def find_max(self, ary):
        max_sum = float('-inf')
        current_sum = 0
        for i in ary:
            current_sum = current_sum + i
            if max_sum < current_sum:
                max_sum = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_sum


sol = Solution()

a = [-13, -3, -25, -20, -3, 8, -6, 25, -5, -22, -15, -4, -7]
mx = sol.find_max(a)
print(mx)


