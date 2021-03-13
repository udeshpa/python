

class Solution(object):
    def rearrage(self,ary):
        N = len(ary)
        smallest = 0
        largest = N -1
        aux_ary = [None] * (N)
        largest_flg = True
        for i in range(0, N):
            if largest_flg:
                print(ary[largest])
                aux_ary[i] = ary[largest]
                largest = largest - 1
                largest_flg = False
            else:
                print('here', ary[smallest])
                aux_ary[i] = ary[smallest]
                smallest = smallest + 1
                largest_flg = True

        return aux_ary


sol = Solution()
print(sol.rearrage([1,2,3,4,5,6,7,8]))
