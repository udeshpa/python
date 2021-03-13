class Solution(object):
    def continuous_add(self, ary, S):
        ps = 0
        st_index = 1
        end_index = 1
        N = len(ary)

        lst = []
        while end_index <= N:
            ps = ps + ary[end_index - 1]
            if ps == S:
                lst.append((st_index, end_index))
            elif ps < S:
                end_index = end_index + 1
            else:
                ps = ps - ary[st_index - 1] - ary[end_index - 1]
                st_index = st_index + 1

                if st_index == end_index:
                    end_index = end_index + 1

        return lst


sol = Solution()

ary = [1,2,3,7,5]
S = 12
print(ary)
pairs = sol.continuous_add(ary, S)

print(pairs)


ary = [1,2,3,4,5,6,7,8,9,10]
S = 15
print(ary)
pairs = sol.continuous_add(ary, S)

print(pairs)




