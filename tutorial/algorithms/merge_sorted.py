class Solution(object):

    def rotate(self, ary1, ary2, i, j):
        N1 = len(ary1)
        N2 = len(ary2)
        print(f'i is {i}, j is {j}')
        if N1-1 >= i:
            tmp = ary1[N1-1]

        for i in range(N1-1, i-1, -1):
            ary1[i] = ary1[i-1]

        tmp1 = ary2[j]
        ary2[j] = tmp
        ary1[i] = tmp1

    def merge(self, ary1, ary2):
        N1 = len(ary1)
        N2 = len(ary2)
        i = 0
        j = 0
        print(f'N1 is {N1} and N2 is {N2}')
        for j in range(N2-1, -1, -1):
            print(j)
            cur2 = ary2[j]
            for i in range(0, N1):
                print(j, i, cur2, ary1[i])
                if cur2 < ary1[i]:
                    self.rotate(ary1, ary2, i, j)
                    print(ary1, ary2)
                    break


sol = Solution()
a = [2, 3, 9, 10, 20]
b = [1, 4, 8, 50, 100]
sol.merge(a, b)

print(a,b)

