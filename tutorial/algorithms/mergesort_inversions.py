
class Solution(object):

    def merge(self, ary, aux, lo, mid, hi):

        #first copy
        for k in range(lo, hi+1):
            aux[k] = ary[k]
        i = lo
        j = mid + 1

        inversioncount = 0

        for k in range(lo, hi+1):
            if i > mid:
                ary[k] = aux[j]
                j = j+1
            elif j > hi:
                ary[k] = aux[i]
                i = i+1
            elif aux[j] < aux[i]:
                ary[k] = aux[j]
                j = j+1
                print(mid, k)
                inversioncount = inversioncount + mid - i + 1
            else:
                ary[k] = aux[i]
                i = i+1

        print(inversioncount)

        return inversioncount

    def sort(self, ary, aux, lo, hi):
        if hi <= lo:
            return 0

        mid = lo + int((hi - lo)/2)
        leftinversions = self.sort(ary, aux, lo, mid)
        rightinversions = self.sort(ary, aux, mid+1, hi)
        inversions = self.merge(ary, aux, lo, mid, hi)
        return leftinversions + rightinversions + inversions

    def mergesort(self, ary):
        N = len(ary)
        aux = [None] * N
        return self.sort(ary, aux, 0, N-1)


sol = Solution()

ary = [2, 4, 1, 3, 5]
ret = sol.mergesort(ary)
print(ary, ret)
