class Solution(object):
    def triplets(self, ary):
        print(ary)
        ary.sort()
        N = len(ary)
        st_index = 0
        end_index = st_index + 1

        lst = []
        if N < 3:
            return lst

        while st_index <= N - 3:
            while end_index <= N - 1:
                ps = ary[st_index] + ary[end_index]
                print(st_index, end_index, ps)
                for i in range(st_index + 2, N):
                    if ps == ary[i]:
                        lst.append((ary[st_index], ary[end_index], ary[i]))
                    continue

                end_index = end_index + 1

            st_index = st_index + 1
            end_index = st_index + 1

        return lst

sol = Solution()

arr = [1, 5, 3, 2]
ret = sol.triplets(arr)
print(ret)

arr = [2,3,4]
ret = sol.triplets(arr)
print(ret)
